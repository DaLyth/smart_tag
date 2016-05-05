#Take a file and output a TF tokenized, stemmed file

import string
import text_tokenizer
import os

def tfBuilder():
	path = input('Enter file location: ')
	doc = open(path, 'r')
	text = doc.read()
	doc.close()
	text = text.lower()
	text = text.translate(None, string.punctuation)
	text = text.translate(None, string.digits)
	tf = text_tokenizer.tokenize(text)
	s = str(tf)
	path = os.getcwd()
	path += '/new/tf.txt'
	doc = open(path, 'w')
	doc.write(s)
	doc.close()

tfBuilder()


