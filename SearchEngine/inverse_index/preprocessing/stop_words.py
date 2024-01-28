import nltk
import string
from nltk.corpus import stopwords

stop_words = set()


def init_stop_words():
    stop_words.update(set(stopwords.words('english')))
    stop_words.update(set(string.punctuation))


def get_stop_words():
    return stop_words
