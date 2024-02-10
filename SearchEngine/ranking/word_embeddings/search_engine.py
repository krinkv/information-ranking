import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from SearchEngine.inverse_index.inverse_index import init_documents_word_embeddings
from SearchEngine.inverse_index.preprocessing.io_util import read_doc


def init_word2vec_model():
    return api.load("word2vec-google-news-300")


def init_engine():
    documents = init_documents_word_embeddings()
    w2v_model = init_word2vec_model()
    return SearchEngine(w2v_model, documents)


class SearchEngine:
    def __init__(self, word2vec_model, documents):
        self.word2vec_model = word2vec_model
        self.documents_vectorized = self.vectorize_docs(documents)

    def vectorize_docs(self, documents):
        doc_vecs = {}

        for doc_id, doc_bag in documents.items():
            doc_vecs[doc_id] = self.vectorize(doc_bag)

        return doc_vecs

    def get_best_documents(self, query_bag):
        candidates = []
        query_vec = self.vectorize(query_bag)

        for doc_id, doc_vec in self.documents_vectorized.items():
            candidates.append((doc_id, self.cosine_similarity(query_vec, doc_vec)))

        sorted_candidates = sorted(candidates,
                                   key=lambda cand: cand[1],
                                   reverse=True)

        previews = []
        for doc_id, _ in sorted_candidates[:10]:
            preview = self.get_document_preview(doc_id)
            previews.append((doc_id, preview[0], preview[1]))

        return previews

    def get_document_preview(self, doc_id):
        doc_sentences = read_doc(doc_id).split('.')
        doc_title = ' '.join(doc_sentences[0].split()[:4]) + "..."

        return doc_title, '.'.join(doc_sentences[:2])

    def vectorize(self, bag):
        return np.mean([self.word2vec_model[word]
                        for word in bag if word in self.word2vec_model],
                       axis=0)

    def cosine_similarity(self, query_vec, doc_vec):
        return cosine_similarity([query_vec], [doc_vec])[0][0]
