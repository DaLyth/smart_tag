import string
import os

def token_dict_builder():
	token_dict = {}
	path = input('Path to the corpus from which to build the dictionary: ')
	for subdir, dirs, files in os.walk(path):
		for file in files:
	        	file_path = subdir + os.path.sep + file
        		shakes = open(file_path, 'r')
        		text = shakes.read()
        		lowers = text.lower()
        		no_punctuation = lowers.translate(None, string.punctuation)
        		token_dict[file] = no_punctuation
	return token_dict
