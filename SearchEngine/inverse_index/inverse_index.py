from nltk.corpus import PlaintextCorpusReader

from SearchEngine.inverse_index.preprocessing.tokenizer import tokenize_document

documents = dict()
index = dict()

CORPUS_DIR = '../resources/'

"""
Initialize the `documents` dictionary that would be:
    doc number -> doc content
To get document content, use the `read_document` function in io-util.py
Consider what "document content" means, i.e.:
    - raw document
    - document with preprocessed words (if we are going to store terms in normalized form). Then,
      if we want to display original document to user, just read it again.
:param paths: a list of paths to documents
:return: Initialized `documents`
"""


def init_documents():
    corpus = PlaintextCorpusReader(CORPUS_DIR, '.*\.txt')

    # corpus.paras returns all paragraphs as each paragraph in corpus.txt is separate document
    raw_documents = corpus.paras()
    for i in range(len(raw_documents)):
        documents[i] = tokenize_document(raw_documents[i])

    return documents


"""
Read content of all docs and preprocess it (i.e. tokenize it, remove stop words, consider form of storing words).
Then initialize `index` dictionary that would be:
word (or term) -> list of numbers of the docs that contain word (or term)
:return: Initialized `index`
"""


def init_index():
    for doc_id in documents:
        for word in documents[doc_id]:
            if word in index:
                index[word].add(doc_id)
            else:
                index[word] = {doc_id}

    return index
