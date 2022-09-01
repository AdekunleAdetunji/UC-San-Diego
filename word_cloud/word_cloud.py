import re
from collections import Counter

def prepare(novelFile, negativeFile):
    '''Function to prepare the text files to be analysed, the variable novel\
    file being the containing group of words and the negativeFile positional\
    kwargs being the file containing words that should not be counted.'''

    novelObj = open(novelFile, 'r', encoding = 'utf-8')
    negativeObj = open(negativeFile, 'r', encoding = 'utf-8')

    novel = novelObj.read().split() #Create a list of word element
    negative = negativeObj.read().split() #Create a list of not needed words

    reObj = re.compile('\W+') # Regex Object to clean words
    target = []
    for word in novel:
        word = reObj.sub('', word.lower())
        if word not in negative: # Conditional to not append non needed words
            target.append(word)
    word_count = Counter(target) # a dictionary of desired word count.
    return word_count
