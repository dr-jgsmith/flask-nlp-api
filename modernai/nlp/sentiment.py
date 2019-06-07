from extensions import TextBlob


def sentiment_blob(text):
    text_object = TextBlob(text)
    sentiment = [(sentence.sentiment.polarity, sentence.sentiment.subjectivity)
                 for sentence in text_object.sentences]
    return sentiment


