import nltk
import string
import os
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer



path = input('Enter path name: ')
token_dict = {}
stemmer = PorterStemmer()
num_files = 0

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

for subdir, dirs, files in os.walk(path):
    for file in files:
	num_files += 1
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation
        
#print token_dict

#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

#print tfs

path2 = input('Enter the text you want to compare: ')

file2 = open(path2, 'r')

text = file2.read()
text = text.lower()
text = text.translate(None, string.punctuation)

response = tfidf.transform([text])

#print response

total = []
for i in range(num_files):
	total.append(0)
	for k in range(tfs[0].toarray()[0].size):
		total[i] += tfs[i].toarray()[0][k]*response.toarray()[0][k]

print token_dict.keys()
print total
