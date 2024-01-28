import nltk
import string
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

from SearchEngine.inverse_index.inverse_index import init_documents, documents, init_index, index
from SearchEngine.inverse_index.preprocessing.stop_words import init_stop_words
from SearchEngine.inverse_index.preprocessing.tokenizer import tokenize_document

# Paths to documents in corpus
PATHS = None
CORPUS_DIR = './resources/news.txt'


def user_interactive_loop():
    # TODO: implement
    pass


if __name__ == '__main__':
    init_stop_words()
    init_documents()
    init_index()