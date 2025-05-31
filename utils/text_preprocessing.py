import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download once only (handled in main.py, not here)
# nltk.download('punkt')
# nltk.download('stopwords')

# --- Text Preprocessing Steps ---

def text_lowercase(text):
    """Convert text to lowercase."""
    return text.lower()

def remove_punctuation(text):
    """Remove punctuation from the text."""
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_whitespace(text):
    """Remove extra spaces from the text."""
    return " ".join(text.split())

def remove_stopwords(text):
    """Remove stopwords using NLTK."""
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return " ".join(filtered_text)

def text_preprocess(text):
    """Full preprocessing pipeline: lowercase, clean, stopword removal."""
    text = text_lowercase(text)
    text = remove_punctuation(text)
    text = remove_whitespace(text)
    text = remove_stopwords(text)
    return text
