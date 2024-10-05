from nltk.tokenize import word_tokenize
import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

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

def lexical_diversity_spacy(sentence):
    # Process the sentence with spaCy to tokenize
    doc = nlp(sentence)
    
    # Extract tokens and ignore punctuation and spaces
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    
    # Calculate number of unique words
    unique_words = set(tokens)
    
    # Lexical diversity = unique words / total words
    lexical_diversity = len(unique_words) / len(tokens) if tokens else 0
    
    return lexical_diversity


def compute_lexical_diversity(sentence):
    nltk_diversity_metric = lexical_diversity_nltk(sentence)
    spacy_diversity_metric = lexical_diversity_spacy(sentence)

    return (nltk_diversity_metric+spacy_diversity_metric)/2



# sentence = """ I can't express the gratitude we all have for this help and for all of the money raised.
#
# This page is being managed as a team of volunteers who are connected to the North Shore. We are contributing to relief efforts on the ground and also working to determine the right way to distribute these funds to everyone affected. It is our hope that we will be able to partner with a local non-profit to provide both short- and long-term relief, and will keep everyone updated as soon as we can. The GoFundMe team is also providing us with amazing support and guidance on how to move forward.
#
# We've been moved by the way the community has come together to support each other. People like Laird Hamilton and Gabby Reece have been out in their boat rescuing people and  we know we are stronger together.
#
# Your donations will help us move past this devastation, and we will remain transparent about how they are being managed. Thank you for your patience as we continue to work out logistics while also doing our part with impacted friends and neighbors. Thank you so much!
#
# Friends of ours have lost their homes. Here is some of what we are seeing in our day-to-day right now:"""
#
#
# nltk_diversity_metric = lexical_diversity_nltk(sentence)
# spacy_diversity_metric = lexical_diversity_spacy(sentence)
#
# print("nltk",nltk_diversity_metric)
# print("spacy",spacy_diversity_metric)
# print("mean", (nltk_diversity_metric+spacy_diversity_metric))