from nltk.tokenize import word_tokenize
#import spacy

# Load spaCy's English language model
#nlp = spacy.load("en_core_web_sm")

# Download required data for tokenization (run only once)
#nltk.download('punkt_tab')


def lexical_diversity_nltk(sentence):
    # Tokenize the sentence into words
    print('here')
    tokens = word_tokenize(sentence)

    # Calculate number of unique words
    unique_words = set(tokens)

    # Lexical diversity = unique words / total words
    lexical_diversity = len(unique_words) / len(tokens) if tokens else 0

    return lexical_diversity

# def lexical_diversity_spacy(sentence):
#     # Process the sentence with spaCy to tokenize
#     doc = nlp(sentence)
#
#     # Extract tokens and ignore punctuation and spaces
#     tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
#
#     # Calculate number of unique words
#     unique_words = set(tokens)
#
#     # Lexical diversity = unique words / total words
#     lexical_diversity = len(unique_words) / len(tokens) if tokens else 0
#
#     return lexical_diversity


def compute_lexical_diversity(sentence):
    nltk_diversity_metric = lexical_diversity_nltk(sentence)
    #spacy_diversity_metric = lexical_diversity_spacy(sentence)

    return nltk_diversity_metric
