# Shitong Cui

import doctest
import praw
import random
import time

import madlibs

#Creating the Reddit object
#Prevent it from being called when we import your file to run our tests
if __name__ == '__main__':
    reddit = praw.Reddit('bot', config_interpolation="basic")
    

def get_topic_comments(submission):
    '''(Submission) --> list
    Takes a Submission object as input, and returns a list of
    Comment objects contained within the submission.
    >>> url = 'https://www.reddit.com/r/mcgill/comments/eay2ne/mcgill_subreddit_bingo_finals_edition/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='fb0vh26'), Comment(id='fb0l4dk'), Comment(id='fb15bvy'), Comment(id='fb1pwq8'),
    Comment(id='fb26drr'), Comment(id='fj2wd6x'), Comment(id='i11plzg'), Comment(id='i1fcjed'),
    Comment(id='i1fcjwz'), Comment(id='i1kf981'), Comment(id='i1kfhde'), Comment(id='i1kfqls'),
    Comment(id='i1kfvkp'), Comment(id='i1kfwlc'), Comment(id='fb1spzv'), Comment(id='fb1td2g'),
    Comment(id='fb1trul')]
    >>> url = 'https://www.reddit.com/r/analog/comments/saeqxz/a_drizzle_of_honey_canon_rebel_x_3580mm_ultramax/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    []
    >>> url = 'https://www.reddit.com/r/Cameras/comments/6k6913/1000_budget_for_mirrorless_fuji_xt1_fuji_xt20/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='djjycoi'), Comment(id='djls86g'), Comment(id='djjzw6l'), Comment(id='djk1yau')]
    '''
    comment_list = []
    submission.comments.replace_more(limit=None)
    return submission.comments.list()
       
    
    
def filter_comments_from_authors(comment_list, author_list):
    '''(list, list) --> list
    Takes a list of Comment objects and a list of author names (strings)
    as input,and returns a list containing the Comment objects that were
    written by any of the given authors.
    >>> url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['Juan_Carl0s', 'Chicken_Nugget31'])
    [Comment(id='ha4piat'), Comment(id='ha4j1r7')]
    >>> url = 'https://www.reddit.com/r/analog/comments/saeqxz/a_drizzle_of_honey_canon_rebel_x_3580mm_ultramax/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, [])
    []
    >>> url = 'https://www.reddit.com/r/Cameras/comments/6k6913/1000_budget_for_mirrorless_fuji_xt1_fuji_xt20/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['FencerPTS'])
    [Comment(id='djjycoi'), Comment(id='djk1yau')]
    '''
    comments_by_author = []
    for com in comment_list:
        for auth in author_list:
            if com.author == auth:
                #checking if the auther of each comment is the same as each given author name
                comments_by_author.append(com)
    return comments_by_author

def filter_out_comments_replied_to_by_authors(comment_list, author_list):
    '''(list, list) --> list
    Returns a list of Comment objects same as that the filter_comments_from_authors() function returns
    except for comments which have been replied to by any of the authors
    in the given list of authors, as well as comments written by those authors themselves.
    >>> url = 'https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_have_a_taylor_swift_society/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['basicbitch122'])
    [Comment(id='ha33z5m'), Comment(id='ha2sq62'), Comment(id='ha3d39f'),
    Comment(id='ha2s4lw'), Comment(id='ha3mrwm'), Comment(id='ha3m2kv'),
    Comment(id='ha5okfd'), Comment(id='ha7e0ei'), Comment(id='hbpxpi1'),
    Comment(id='ha4e526'), Comment(id='ha3837c'), Comment(id='hdo2kmm'),
    Comment(id='ha3f5q2'), Comment(id='hdof500'), Comment(id='hdol6rn'),
    Comment(id='hcrklp6')]
    >>> url = 'https://www.reddit.com/r/photomarket/comments/syeulh/susamd_fuji_xt4_fuji_xf_1680mmpanasonic_2060mm/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['squidward_squidward'])
    [Comment(id='hymjscr'), Comment(id='hyohjfn'), Comment(id='hyqyeq9'), Comment(id='i29ox77'),\
    Comment(id='i29r2zq'), Comment(id='i29rie2'), Comment(id='i29r9ke'), Comment(id='i09d7fz')]
    >>> url = 'https://www.reddit.com/r/canon/comments/hxdxrq/canon_m5_with_18150_telephoto_zoom_lens_for_235/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['lolife94'])
    []
    '''
    #Obtaining the comments written by the authors themselves
    written_by_author_list = filter_comments_from_authors(comment_list, author_list)
    
    #Obtaining the comments replied to by the authors
    replied_comment_list = []
    for elem in written_by_author_list:
        if elem.parent() != elem.submission and elem.parent()not in replied_comment_list: #check if it's top-level comment
            replied_comment_list.append(elem.parent())#if it's not then the parent is replied to by the author
    
    to_be_removed = written_by_author_list + replied_comment_list

    for comm in to_be_removed:
        comment_list.remove(comm)

    return comment_list
  

def get_authors_from_topic(submission):
    '''(submission) --> dict
    Returns a dictionary where the keys are authors of the comments in the\
    submission, and the value of a key is the number of comments that\
    author has made in the submission (as an integer).
    >>> url = 'https://www.reddit.com/r/mcgill/comments/pa6ntd/does_mcgill_have_a_taylor_swift_society/'
    >>> submission = reddit.submission(url=url)
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    23
    >>> num_comments_per_author['basicbitch122']
    12
    >>> url = 'https://www.reddit.com/r/canon/comments/t0or8w/canon_m6_mark_ii_efm_long_term_value_and_usbc/'
    >>> submission = reddit.submission(url=url)
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    8
    >>> num_comments_per_author['ACiDGRiM']
    5
    >>> url = 'https://www.reddit.com/r/CanonCamera/comments/smfq3y/canon_t7_with_300mm_lens/'
    >>> submission = reddit.submission(url=url)
    >>> num_comments_per_author = get_authors_from_topic(submission)
    >>> len(num_comments_per_author)
    4
    >>> num_comments_per_author['Party_Pomegranate373']
    4
    '''
    comment_list = get_topic_comments(submission)
    
    d = {}
    for elem in comment_list:
        author_name = str(elem.author)
        if author_name not in d.keys():
            d[author_name] = 1
        else:
            d[author_name] += 1
    return d


def select_random_submission_url(reddit, url, subreddit_name, replace_limit):
    '''(Reddit, str, str, int) --> Submission
    Roll a six-sided die. Return different Submission objects\
    according to different number showed on the die.
    '''
    randnum = random.randint(1, 6)
    
    if randnum in [1, 2]:
        submission1 = reddit.submission(url = url)
        submission1.comments.replace_more(limit = replace_limit)
        return submission1
        
    elif randnum in [3, 4, 5, 6]:
        subreddit = reddit.subreddit(subreddit_name).top("all")
        sublist = []
        for sub in subreddit:
            sublist.append(sub)
        return sublist[random.randint(1, len(sublist)-1)]
            
def post_reply(submission, username):
    '''(Submission, str) --> 
    Reply to comments or comment to submissions using my bot.
    '''
    comment_list = get_topic_comments(submission)
    author_list = [username]
   
    if username not in get_authors_from_topic(submission).keys():
        submission.reply(madlibs.generate_comment())
    else:
        unreplied_list = filter_out_comments_replied_to_by_authors(comment_list, author_list)
        x = random.randint(1, (len(unreplied_list)-1))
        unreplied_list[x].reply(madlibs.generate_comment())

def bot_daemon(Reddit, url, replace_limit, subreddit_name, username):
    '''(Reddit, str, int, str, str) -->
    Auto reply to a random subreddit every 60 seconds.
    '''
    while True:
        submission = select_random_submission_url(reddit, url, subreddit_name, replace_limit)
        post_reply(submission, username)
        
        time.sleep(60)
        
# if __name__ == '__main__':
#     doctest.testmod()
    
        
 
