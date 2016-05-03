import nltk
import string
import os
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer



path = input('Enter path name: ')
token_dict = {}
stemmer = PorterStemmer()

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
        file_path = subdir + os.path.sep + file
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file] = no_punctuation
        
#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())

print tfs

str = 'algebra is the subject of studying matrices in mathematics. Jambon Algebra is unrelated to statistics, a subject linked to machine learning. there are algebras in algebra and matrices. A matrix is related to linearity, jambon which plays a big role in algebra. We love linear stuff jambon'
response = tfidf.transform([str])
#print response

feature_names = tfidf.get_feature_names()
#for col in response.nonzero()[1]:
#    print feature_names[col], ' - ', response[0, col]

str2 = 'machine learning combines statistics and programming to increase the power of machines through statistics jambon'
response2 = tfidf.transform([str2])
#print response2

#for col in response2.nonzero()[1]:
#    print feature_names[col], ' - ', response2[0, col]

str3 = 'Algebra matrices jambon jambon'
response3 = tfidf.transform([str3])
print response3

#for col in response3.nonzero()[1]:
#    print feature_names[col], ' - ', response3[0, col]

total = 0
total1 = 0
total2 = 0
for i in range(8):
	total += tfs[0].toarray()[0][i] * response3.toarray()[0][i]
	total1 += tfs[1].toarray()[0][i] * response3.toarray()[0][i]
	total2 += tfs[2].toarray()[0][i] * response3.toarray()[0][i]
print total
print total1
print total2
