import nltk
import string

from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *

file_name = input('Enter file location to tag: ')

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def get_tokens():
   with open(file_name, 'r') as shakes:
    text = shakes.read()
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
count = Counter(tokens)

filtered = [w for w in tokens if not w in stopwords.words('english')]
count = Counter(filtered)

stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count = Counter(stemmed)
print count.most_common(100)
