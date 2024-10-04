import wordfreq
from backend.tokenizer import tokenize_sentence

def word_rarity_score(word, lang='en', corpus='large'):
    """
    Returns the rarity score of a word based on its frequency.
    
    The frequency is measured using the wordfreq library.
    The 'large' corpus includes large datasets like Common Crawl.
    
    Args:
    - word (str): The word to score.
    - lang (str): Language of the word (default is 'en' for English).
    - corpus (str): Corpus size to use ('small', 'large', 'twitter').

    Returns:
    - rarity_score (float): A measure of the word's rarity. Lower frequencies give higher scores.
    """
    # Get the frequency of the word in the specified language and corpus
    freq = wordfreq.word_frequency(word, lang, wordlist=corpus)
    
    if freq == 0:
        # If the word is not found, assign a high rarity score (very rare word)
        return 100  # Arbitrary high score for unseen/rare words
    else:
        # Inverse frequency can be used to measure rarity: lower frequency -> higher score
        # Taking the negative log of frequency provides a better rarity metric
        return -wordfreq.zipf_frequency(word, lang, wordlist=corpus)

def score_words(word_list, lang='en', corpus='large'):
    """
    Scores a list of words based on their rarity in the given language and corpus.
    
    Args:
    - word_list (list): List of words to score.
    - lang (str): Language of the words (default is 'en').
    - corpus (str): Corpus size ('small', 'large', 'twitter').
    
    Returns:
    - scores (dict): A dictionary with words as keys and their rarity scores as values.
    """
    scores = {}
    for word in word_list:
        scores[word] = word_rarity_score(word, lang=lang, corpus=corpus)
    return scores

sentence = """ I can't express the gratitude we all have for this help and for all of the money raised.

This page is being managed as a team of volunteers who are connected to the North Shore. We are contributing to relief efforts on the ground and also working to determine the right way to distribute these funds to everyone affected. It is our hope that we will be able to partner with a local non-profit to provide both short- and long-term relief, and will keep everyone updated as soon as we can. The GoFundMe team is also providing us with amazing support and guidance on how to move forward.

We've been moved by the way the community has come together to support each other. People like Laird Hamilton and Gabby Reece have been out in their boat rescuing people and  we know we are stronger together.

Your donations will help us move past this devastation, and we will remain transparent about how they are being managed. Thank you for your patience as we continue to work out logistics while also doing our part with impacted friends and neighbors. Thank you so much!

Friends of ours have lost their homes. Here is some of what we are seeing in our day-to-day right now:"""

words = tokenize_sentence(sentence)
rarity_scores = score_words(words, lang='en', corpus='large')

for word, score in rarity_scores.items():
    print(f"Word: {word}, Rarity Score: {score}")
