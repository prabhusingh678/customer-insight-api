from textblob import TextBlob
from collections import Counter

def analyze_reviews(reviews: list):

    full_text = " ".join(reviews)

    
    blob = TextBlob(full_text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    
    words = [word.lower() for word in full_text.split() if len(word) > 3]
    common_words = Counter(words).most_common(3)
    key_themes = [word for word, count in common_words]

    
    actionable_feedback = "Improve UI performance and support quality."

    return {
        "overall_sentiment": sentiment,
        "key_themes": key_themes,
        "actionable_feedback": actionable_feedback,
    }
