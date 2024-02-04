from collections import Counter

from nltk.corpus import PlaintextCorpusReader

from SearchEngine.inverse_index.preprocessing.tokenizer import preprocess_document

documents = dict()
index = dict()

CORPUS_DIR = '../resources/corpus'

"""
Initialize the `documents` dictionary that would be:
    doc_id -> (dictionary of:
                    term -> number of occurrences of term in doc)
:param paths: a list of paths to documents
:return: Initialized `documents`
"""


def init_documents():
    corpus = PlaintextCorpusReader(CORPUS_DIR, '.*\.txt')
    document_names = corpus.fileids()

    for doc_id, doc_name in enumerate(document_names):
        words = corpus.words(doc_name)
        tokenized = preprocess_document(words)
        documents[doc_id] = Counter(tokenized)

    return documents


"""
Initialize `index` dictionary that would be:
term -> list of ids of the docs that contain term
:return: Initialized `index`
"""


def init_index():
    for doc_id in documents:
        for word, _ in documents[doc_id].items():
            if word.isalnum():
                if word in index:
                    index[word].add(doc_id)
                else:
                    index[word] = {doc_id}

    return index
