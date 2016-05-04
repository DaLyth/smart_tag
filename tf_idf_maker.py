import text_tokenizer
import token_dict_builder
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidfer():
	token_dict = token_dict_builder()
	tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
	tfs = tfidf.fit_transform(token_dict.values())
