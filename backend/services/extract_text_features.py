from backend.services.sentiment_analysis.sentiment_analysis import get_sentiment_analysis
from backend.services.sentence_complexity.lexical_complexity import compute_lexical_diversity
from backend.services.word_complexity.word_complexity import compute_word_complexity
from backend.services.tokenizer import tokenize_sentence


result = {
    "Self-reference": 0, #
    "Other-reference":0, #
    "Past orientation":0,
    "Present orientation":0,
    "Future orientation":0,
    "Length":0,
    "Word complexity":0, #
    "Sentence complexity":0, #
    "Certainty":0, #
    "Uncertainty":0, #
    "Positive emotion":0, #
    "Negative emotion":0 #
}
def extract_fetures(sentence):

    # words complexity
    word_features = compute_word_complexity(sentence)
    print(word_features)
    result['Self-reference'] = float(word_features['self_reference'])
    result['Other-reference'] = float(word_features['other_reference'])

    tense_dict = word_features.get('tense',None)
    if not tense_dict:
        result['Past orientation'] = float(word_features['past'])
        result['Present orientation'] = float(word_features['present'])
        result['Future orientation'] = float(word_features['future'])
    else:
        result['Past orientation'] = float(word_features['tense']['past'])
        result['Present orientation'] = float(word_features['tense']['present'])
        result['Future orientation'] = float(word_features['tense']['future'])

    result['Word complexity'] = float(word_features['complexity'])
    result['Certainty'] = float(word_features['certainty'])
    result['Uncertainty'] = float(word_features['uncertainty'])

    # sentence complexity
    sentence_complexity = compute_lexical_diversity(sentence)
    result['Sentence complexity'] = float(sentence_complexity)


    # sentiment analysis
    #positive, neutral, negative = get_sentiment_analysis(sentence)
    res = get_sentiment_analysis(sentence)
    result['positive_emotion'] = res[2]['score']
    result['negative_emotion'] = res[0]['score']

    # lenght
    sentence_lenght = len(tokenize_sentence(sentence))
    result['Length'] = float(sentence_lenght/1000)

    return result

#

