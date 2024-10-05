import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def get_tree_depth_spacy(token):
    """Recursively calculate the depth of a dependency tree."""
    if not list(token.children):  # If the token has no children, return 0
        return 0
    else:
        return 1 + max(get_tree_depth_spacy(child) for child in token.children)

def quantify_syntax_complexity_spacy(sentence):
    # Process the sentence with spaCy
    doc = nlp(sentence)
    
    # Find the root of the dependency tree
    root = [token for token in doc if token.head == token][0]
    
    # Calculate the depth of the dependency tree
    tree_depth = get_tree_depth_spacy(root)
    
    # Return complexity as depth of the dependency tree
    return tree_depth

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
# spacy_syntax_complexity = quantify_syntax_complexity_spacy(sentence)
#
#
# print("nltk",spacy_syntax_complexity)

