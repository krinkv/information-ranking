import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def init_word2vec_model():
    return api.load("word2vec-google-news-300")


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

        return sorted_candidates[:15]

    def vectorize(self, bag):
        return np.mean([self.word2vec_model[word]
                        for word in bag if word in self.word2vec_model],
                       axis=0)

    def cosine_similarity(self, query_vec, doc_vec):
        return cosine_similarity([query_vec], [doc_vec])[0][0]
