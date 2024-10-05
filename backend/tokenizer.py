from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

def tokenize_sentence(sentence):
    tokens = word_tokenize(sentence)
    return tokens

def tokenize_and_remove_stopwords(sentence):
    tokenized_sentence = tokenize_sentence(sentence)
    filtered_words = [word for word in tokenized_sentence if word.lower() not in stopwords.words('english')]
    return filtered_words
