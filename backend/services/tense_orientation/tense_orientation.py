import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Temporal adverbs and time expressions lists
TEMPORAL_ADVERBS = {
    "present": ["now", "today", "currently", "presently", "at the moment", "right now", "this instant", "as of now",
                "at present", "just now", "as we speak", "for the time being"],

    "past":["yesterday", "previously", "formerly", "earlier", "before", "recently", "once", "in the past", "back then",
            "long ago", "lately", "at one time", "the other day"],

    "future":["tomorrow", "soon", "later", "eventually", "in the future", "next", "someday", "shortly", "in a while",
              "in time", "in the near future", "sooner or later", "by and by"]
}

TEMPORAL_NOUN_PHRASES = {"next week", "last year", "this year", "next month", "last month", "in the future",
                         "in the past", "the 1990s", "the future"}


def calculate_verb_tense_percentage(sentence):
    doc = nlp(sentence)

    # Initialize counters
    present_count = 0
    past_count = 0
    future_count = 0
    total_verbs = 0

    # Temporal elements counters
    temporal_adverbs_count = 0
    temporal_nouns_count = 0

    # Iterate over the tokens in the sentence
    for token in doc:
        if token.pos_ == "VERB":  # Check if the token is a verb
            total_verbs += 1

            # Check the tense of the verb
            if "Tense=Pres" in token.morph:
                present_count += 1
            elif "Tense=Past" in token.morph:
                past_count += 1
            elif token.text in ["will", "shall", "might", "should", "could" ]:  # Simple future tense indicator
                future_count += 1

        # Check for temporal adverbs
        if token.text.lower() in TEMPORAL_ADVERBS['present']:
            temporal_adverbs_count += 1

        if token.text.lower() in token.morph:
            present_count += 1
        elif "Tense=Past" in token.morph:
            past_count += 1
        elif token.text in ["will", "shall", "might", "should", "could"]:  # Simple future tense indicator
            future_count += 1

    # Check for temporal noun phrases (multi-word expressions)
    sentence_text = sentence.lower()  # Make sentence lowercase for matching multi-word expressions
    for phrase in TEMPORAL_NOUN_PHRASES:
        if phrase in sentence_text:
            temporal_nouns_count += 1

    # Avoid division by zero if there are no verbs
    if total_verbs == 0:
        return {
            "present_percentage": 0,
            "past_percentage": 0,
            "future_percentage": 0,
            "temporal_adverbs_count": temporal_adverbs_count,
            "temporal_nouns_count": temporal_nouns_count
        }

    # Calculate percentages
    present_percentage = (present_count / total_verbs) * 100
    past_percentage = (past_count / total_verbs) * 100
    future_percentage = (future_count / total_verbs) * 100

    return {
        "present_percentage": present_percentage,
        "past_percentage": past_percentage,
        "future_percentage": future_percentage,
        "temporal_adverbs_count": temporal_adverbs_count,
        "temporal_nouns_count": temporal_nouns_count
    }


# Example sentence
sentence = "I will travel tomorrow, but I visited my friend yesterday and I am working today. Next week, I will be on vacation."
result = calculate_verb_tense_percentage(sentence)
print(result)