from nltk.tokenize import word_tokenize

def tokenize_sentence(sentence):
    """
    Tokenizes a sentence into individual words.
    
    Args:
    - sentence (str): The input sentence to tokenize.
    
    Returns:
    - tokens (list): A list of words (tokens).
    """
    tokens = word_tokenize(sentence)
    return tokens