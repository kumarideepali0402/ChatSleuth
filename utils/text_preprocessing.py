import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def text_lowercase(text):
   
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_whitespace(text):
    return " ".join(text.split())

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return " ".join(filtered_text)

def text_preprocess(text):
    text = text_lowercase(text)
    text = remove_punctuation(text)
    text = remove_whitespace(text)
    text = remove_stopwords(text)
    return text
