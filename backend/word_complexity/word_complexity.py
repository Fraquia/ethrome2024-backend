import numpy as np
from fastembed import TextEmbedding
from sklearn.metrics.pairwise import cosine_similarity
from backend.tokenizer import tokenize_sentence, tokenize_and_remove_stopwords
import time


top_100_common_words = [
    "a", "about", "all", "also", "and", "as", "at", "be", "because", "but",
    "by", "can", "come", "could", "day", "do", "even", "find", "first", "for",
    "from", "get", "give", "go", "have", "he", "her", "here", "him", "his",
    "how", "I", "if", "in", "into", "it", "its", "just", "know", "like", "look",
    "make", "man", "many", "me", "more", "my", "new", "no", "not", "now", "of",
    "on", "one", "only", "or", "other", "our", "out", "people", "say", "see",
    "she", "so", "some", "take", "tell", "than", "that", "the", "their", "them",
    "then", "there", "these", "they", "thing", "think", "this", "those", "time",
    "to", "two", "up", "use", "very", "want", "way", "we", "well", "what", "when",
    "which", "who", "will", "with", "would", "year", "you", "your"]

#model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
embedding_model = TextEmbedding()
embeddings_list = list(embedding_model.embed(top_100_common_words))


def word_rarity(word_vector):
    """Calculate the rarity of a word based on its distance from common words."""

    #word_vector = model[word]
    common_vectors = list(embedding_model.embed(top_100_common_words))

    if len(common_vectors) == 0:
        return 1.0

    # Calculate cosine similarities between the word and common words
    #word_vector = list(embedding_model.embed(word))
    similarities = cosine_similarity([word_vector], common_vectors)
    # Rarity is defined as 1 - average similarity to common words
    return 1 - np.mean(similarities)


def word_complexity_semantic(text):
    words = tokenize_and_remove_stopwords(text)
    emdebbed_words = list(embedding_model.embed(words))

    # Pre-compute complexities
    complexities = np.array([word_rarity(word_vector) for word_vector in emdebbed_words])

    return complexities.tolist()


# Classify words based on their semantic complexity
sentence = """ I can't express the gratitude we all have for this help and for all of the money raised.

This page is being managed as a team of volunteers who are connected to the North Shore. We are contributing to relief efforts on the ground and also working to determine the right way to distribute these funds to everyone affected. It is our hope that we will be able to partner with a local non-profit to provide both short- and long-term relief, and will keep everyone updated as soon as we can. The GoFundMe team is also providing us with amazing support and guidance on how to move forward.

We've been moved by the way the community has come together to support each other. People like Laird Hamilton and Gabby Reece have been out in their boat rescuing people and  we know we are stronger together.

Your donations will help us move past this devastation, and we will remain transparent about how they are being managed. Thank you for your patience as we continue to work out logistics while also doing our part with impacted friends and neighbors. Thank you so much!

Friends of ours have lost their homes. Here is some of what we are seeing in our day-to-day right now:"""

start_time = time.time()
sentence = " ".join(tokenize_and_remove_stopwords(sentence))
complexities = word_complexity_semantic(sentence)
end_time = time.time()

print(sum(complexities)/len(complexities))
print(end_time-start_time)

