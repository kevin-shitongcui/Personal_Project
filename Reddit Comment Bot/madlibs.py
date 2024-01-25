#Shitong Cui

import doctest
import random
import pickle

#Thie following piece code stores a dict obj into a pickled file.

def capitalize_sentences(s):
    '''Takes a string as input containing a number of sentences, and returns
    the string with the first letter of each sentence capitalized.
    >>> capitalize_sentences("hello. hello! hello???? HI!")
    'Hello. Hello! Hello???? HI!'
    >>> capitalize_sentences("hi are you Okey?")
    'Hi are you Okey?'
    >>> capitalize_sentences("...hi")
    '...hi'
    '''
    wordlist = s.split()
    for i, elem in enumerate(wordlist):
        if elem[-1] in '.?!' and i < (len(wordlist)-1):
            wordlist[i + 1] = wordlist[i + 1][0].upper() + wordlist[i+1][1:]
    wordlist[0] = wordlist[0][0].upper() + wordlist[0][1:]     
    return ' '.join(wordlist)
      
def capitalize_sentence_grid(original_list):
    '''(list) --> list
    Returns a list with the same value as the nested list, but with the first
    letter of the first word of each new sentence capitalized.
    >>> grid = [["you", "might", "think"], ["these", "are", "separate", "sentences"], \
    ["but", "they", "are", "not!", "ok,", "this"], ["one", "is."]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'might', 'think'], ['these', 'are', 'separate', 'sentences'], \
    ['but', 'they', 'are', 'not!', 'Ok,', 'this'], ['one', 'is.']]
    >>> grid = [["you", "are", "right."]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'are', 'right.']]
    >>> grid = [["you", "are", "taking"], ["COMP202!", "good", "for", "you."], ["i", "think", "so."]]
    >>> capitalize_sentence_grid(grid)
    [['You', 'are', 'taking'], ['COMP202!', 'Good', 'for', 'you.'], ['I', 'think', 'so.']]
    '''
    w_list = []
    for elem in original_list:
        sublist = []
        for i in elem:
            sublist.append(i)
        w_list.append(sublist)
            
    w_list[0][0] = w_list[0][0].capitalize()
    for x, sublist in enumerate(w_list):
        for i, elem in enumerate(sublist):
            if elem[-1] in '.?!':
                if i != (len(sublist)-1):   #if the character is not at the last element of a sublist
                    sublist[i + 1] = sublist[i + 1][0].upper() + sublist[i + 1][1:]
                else:
                    if x+1<len(w_list): #if it is, move on the the next sublist, if there is one
                        w_list[x+1][0] = w_list[x+1][0][0].upper() + w_list[x+1][0][1:]
    return w_list

def fill_in_madlib(mls, d):
    '''(str, dict) --> str
    Returns the filled in madlib string.
    >>> random.seed(9004)
    >>> d = {'COLOR': ['yellow', 'glowing green', 'red'], 'VEHICLE': ['hoverboard', \
                      'sportscar', 'electric bike', 'starship']}
    >>> fill_in_madlib("Wow! Is that a [COLOR] [VEHICLE]?", d)
    'Wow! Is that a glowing green starship?'
    
    >>> random.seed(2022)
    >>> d = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled', 'studied'], \
                      'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], \
                                 [ADJECTIVE_2] and [ADJECTIVE_3],", d)
    'Once upon a midnight lazy, while I studied, starry and lazy,'
    >>> random.seed(2022)
    >>> d = ['pondered', 'scribbled', 'snoozled', 'studied', 'dreamy', 'weak', 'weary', 'starry', 'lazy']
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], \
                                 [ADJECTIVE_2] and [ADJECTIVE_3],", d)
    Traceback (most recent call last):
      File "<pyshell>", line 2, in <module>
      File "/Users/cuishitong/Desktop/COMP202 Assignment 3/Assignment files/madlibs.py", line 81, in fill_in_madlib
        raise AssertionError ('The second input(d) should be a Dictionary with type dict.')
    AssertionError: The second input(d) should be a Dictionary with type dict.
    >>> random.seed(2022)
    >>> d = {'PAST-TENSE-VERB': ['pondered', 'scribbled', 'snoozled', 'studied'], \
                      'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib(3, d)
    Traceback (most recent call last):
      File "<pyshell>", line 1, in <module>
      File "/Users/cuishitong/Desktop/COMP202 Assignment 3/Assignment files/madlibs.py", line 83, in fill_in_madlib
        raise AssertionError ('The first input(mls) should be a string.')
    AssertionError: The first input(mls) should be a string.
    >>> random.seed(2022)
    >>> d = {5: ['pondered', 'scribbled', 'snoozled', 'studied'], \
                      'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], \
                                 [ADJECTIVE_2] and [ADJECTIVE_3],", d)
    Traceback (most recent call last):
      File "<pyshell>", line 2, in <module>
      File "/Users/cuishitong/Desktop/COMP202 Assignment 3/Assignment files/madlibs.py", line 104, in fill_in_madlib
        raise AssertionError ('All the keys in the second input(d) should be string.')
    AssertionError: All the keys in the second input(d) should be string.
    >>> random.seed(2022)
    >>> d = {'PAST-TENSE-VErb': ['pondered', 'scribbled', 'snoozled', 'studied'], \
                      'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], \
                                 [ADJECTIVE_2] and [ADJECTIVE_3],", d)
    Traceback (most recent call last):
      File "<pyshell>", line 2, in <module>
      File "/Users/cuishitong/Desktop/COMP202 Assignment 3/Assignment files/madlibs.py", line 106, in fill_in_madlib
        raise AssertionError ('All the keys in the second input(d) should be in upper cases.')
    AssertionError: All the keys in the second input(d) should be in upper cases.
    >>> random.seed(2022)
    >>> d = {'PAST-TENSE-VERB': 5, \
                      'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], \
                                 [ADJECTIVE_2] and [ADJECTIVE_3],", d)
    Traceback (most recent call last):
      File "<pyshell>", line 2, in <module>
      File "/Users/cuishitong/Desktop/COMP202 Assignment 3/Assignment files/madlibs.py", line 136, in fill_in_madlib
        raise AssertionError ('All the values in d should be lists.')
    AssertionError: All the values in d should be lists. 
    >>> random.seed(2022)
    >>> d = {'PAST-TENSE-VERB': [3, 'scribbled', 'snoozled', 'studied'], \
                      'ADJECTIVE': ['dreamy', 'weak', 'weary', 'starry', 'lazy']}
    >>> fill_in_madlib("Once upon a midnight [ADJECTIVE_1], while I [PAST-TENSE-VERB], \
                                 [ADJECTIVE_2] and [ADJECTIVE_3],", d)
    Traceback (most recent call last):
      File "<pyshell>", line 2, in <module>
      File "/Users/cuishitong/Desktop/COMP202 Assignment 3/Assignment files/madlibs.py", line 142, in fill_in_madlib
        raise AssertionError ('All the words in the lists of words(namely the values of d) should be string.')
    AssertionError: All the words in the lists of words(namely the values of d) should be string.
    '''

    if type(d) != dict:
        raise AssertionError ('The second input(d) should be a Dictionary with type dict.')
    if type(mls) != str:
        raise AssertionError ('The first input(mls) should be a string.')
    for key in d:
        if type(key) != str:
            raise AssertionError ('All the keys in the second input(d) should be string.')
        if key != key.upper():
            raise AssertionError ('All the letters of the keys in the second input(d) should be in upper cases.')
        if type(d[key]) != list:
            raise AssertionError ('All the values in d should be lists.')
        for elem in d[key]:
            if type(elem) != str:
                raise AssertionError ('All the words in the lists of words(namely the values of d) should be string.')        
    wd = {}
    for key in d:
        wd[key] = d[key][:] #performing deep copy

    mls_list = mls.split()
    for i, elem in enumerate(mls_list):
        if '[' in elem and ']' in elem and elem.upper() == elem:
            
            punctuation= '\'!()-{};:\"\,<>./?@#$%^&*_~'
            if elem[-1] in punctuation:   
                blank_space = elem[1 : -2]  #removing punctuation
                
                punct = elem[-1]
            
                if blank_space in wd.keys():
                    mls_list[i] = wd[blank_space][random.randint(0, (len(wd[blank_space]) - 1))] + punct      
                else:
                    blank_space = blank_space[:-2]
                    mls_list[i] = wd[blank_space][random.randint(0, (len(wd[blank_space]) - 1))] + punct
                    del wd[blank_space][random.randint(0, (len(wd[blank_space]) - 1))]         
            else:
                blank_space = elem[1 : -1]
                
                if blank_space in wd.keys():
                    mls_list[i] = wd[blank_space][random.randint(0, (len(wd[blank_space]) - 1))]    
                else:
                    blank_space = blank_space[:-2]
                    mls_list[i] = wd[blank_space][random.randint(0, (len(wd[blank_space]) - 1))]
                    del wd[blank_space][random.randint(0, (len(wd[blank_space]) - 1))]
    
    return ' '.join(mls_list)

def load_and_process_madlib(file_name):
    '''(str) --> 
    Takes as input a filename corresponding to a file that\
    contains a madlib string and returns nothing. Save the\
    string to the file 'madlibk_filled.txt'.
    >>> random.seed(2022)
    >>> load_and_process_madlib('madlib1.txt')
    >>> f = open('madlib1_filled.txt', 'r')
    >>> s = f.read()
    >>> s
    'Once upon a midnight lazy, while I studied, starry and lazy,'
    >>> random.seed(2019)
    >>> load_and_process_madlib('madlib1.txt')
    >>> f = open('madlib1_filled.txt', 'r')
    >>> s = f.read()
    >>> s
    'Once upon a midnight weak, while I studied, weary and lazy,'
    >>> random.seed(2002)
    >>> load_and_process_madlib('madlib1.txt')
    >>> f = open('madlib1_filled.txt', 'r')
    >>> s = f.read()
    >>> s
    'Once upon a midnight dreamy, while I snoozled, dreamy and weak,'
    
    '''
    filename = file_name
    fobj = open(filename, 'r')
    madlib_str = fobj.read()
    fobj.close()
    
    f = open('word_dict.pkl', 'rb')
    word_dict = pickle.load(f) # word_dict (type dict)
    f.close()

    new_file_name = file_name[:-4] + '_filled.txt' #Generat the file name of the new file

    final_fobj = open(new_file_name, 'w')
    final_fobj.write(fill_in_madlib(madlib_str, word_dict))
    final_fobj.close()


def generate_comment():
    '''() --> str
    Chooses a random number k between 1 and 10, and reads in the madlib string
    contained in the file at madlibk.txt, fills in the madlib string using the
    word dictionary at word_dict.pkl, and then returns the string that was saved
    to the file madlibk_filled.txt
    >>> random.seed(9001)
    >>> generate_comment()
    'Every student in Mcgill, no matter if you are a psychology , arts , \
    engineering , anthropology or engineering student, as long as you are\
    taking cs courses, it is time for us to vote. It is our time!'
    >>> random.seed(2002)
    >>> generate_comment()
    'Every student in Mcgill, no matter if you are a anthropology , management ,\
    anthropology , management or engineering student, as long as you are taking\
    cs courses, it is time for us to vote. It is our time!'
    >>> random.seed(2019)
    >>> generate_comment()
    'Log on to the CSSSMU website and vote for the candidate that you find \
    reliable! Take the future of CS in your own hands.'
    '''
    x = random.randint(1, 10)
    
    #Generating random file name
    file_name = 'madlib' + str(x) + '.txt'
    
    load_and_process_madlib(file_name)
    
    f_name = file_name[:-4] + '_filled.txt'
    
    fobj = open(f_name, 'r')
    text = fobj.read()
    fobj.close()
    
    return text
    

