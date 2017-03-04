#Takes a file and writes the tf-idf values into another file labeled tf_files/tf_name_of_your_file
#This program needs to be in the same folder as the idf_base file

import nltk
import sys
import string
import unicodedata
import numpy as np
import os

from nltk.stem.porter import *
from nltk.corpus import stopwords

def file_cleaner(path):
	file1 = open(path, 'r')
	text = file1.read()
	file1.close()
	text = text.encode('ascii','ignore')
	text = text.lower()
	text = text.translate(None, string.punctuation)
	text = text.translate(None, string.digits)
	text = string.replace(text, '\n', ' ')
	return text

def stem_tokens(tokens, stemmer):
	stemmed = []
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	return stemmed

def get_tokens(text, stemmer):
	tokens = nltk.word_tokenize(text)
	filtered = [w for w in tokens if not w in stopwords.words('english')]
	stems = stem_tokens(filtered, stemmer)
	return stems

def main(text):
	stemmer = PorterStemmer()
	tokens = get_tokens(text, stemmer)
	return tokens

path = sys.argv[1]

dict_file = open('string_to_int', 'r')
dictionary = eval(dict_file.read())
dict_file.close()

path_idf = 'idf_base'      #Can be changed if the idf_base is in another folder
idf_base = open(path_idf, 'r')
idf_array = idf_base.read().split('\n')
idf_base.close()

cleaned = file_cleaner(path)

tokens = main(cleaned)
tokens, amount = np.unique(tokens, return_counts=True)

tf_file = open('./tf_files/tf_' + os.path.basename(path), 'w')

for x in range(len(tokens)):
	key = tokens[x].encode('ascii','ignore')
	if dictionary.has_key(key):
		int_value = dictionary[key]
		tf_count = amount[x]
		idf = float(idf_array[int_value].lstrip(str(int_value) + ','))
		tf_file.write(str(int_value) + ',' + str(tf_count*idf) + '\n')

tf_file.close()
