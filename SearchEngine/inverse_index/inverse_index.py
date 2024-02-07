from collections import Counter

from nltk.corpus import PlaintextCorpusReader

from SearchEngine.inverse_index.preprocessing.tokenizer import preprocess_document

documents_tf_idf = dict()
documents_word_embeddings = dict()
index = dict()

CORPUS_DIR = '../resources/corpus'

"""
Initialize the `documents` dictionary that would be:
    doc_id -> (dictionary of:
                    term -> number of occurrences of term in doc)
:param paths: a list of paths to documents
:return: Initialized `documents`
"""


def init_documents_if_idf():
    corpus = PlaintextCorpusReader(CORPUS_DIR, '.*\.txt')
    document_names = corpus.fileids()

    for doc_id, doc_name in enumerate(document_names):
        words = corpus.words(doc_name)
        tokenized = preprocess_document(words)
        documents_tf_idf[doc_id] = Counter(tokenized)

    return documents_tf_idf


"""
Initialize `documents` dictionary that would be:
    doc_id -> list of terms in doc
"""


def init_documents_word_embeddings():
    corpus = PlaintextCorpusReader(CORPUS_DIR, '.*\.txt')
    document_names = corpus.fileids()

    for doc_id, doc_name in enumerate(document_names):
        words = corpus.words(doc_name)
        documents_word_embeddings[doc_id] = preprocess_document(words)

    return documents_word_embeddings


"""
Initialize `index` dictionary that would be:
term -> list of ids of the docs that contain term
:return: Initialized `index`
"""


def init_index():
    for doc_id in documents_tf_idf:
        for word, _ in documents_tf_idf[doc_id].items():
            if word.isalnum():
                if word in index:
                    index[word].add(doc_id)
                else:
                    index[word] = {doc_id}

    return index
