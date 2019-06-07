from extensions import text_process


def get_topics(text):
    text_process.load_sequence(text)
    topics = text_process.rank_words_phrases()
    return topics
