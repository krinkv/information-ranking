import gensim.downloader as api
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def init_word2vec_model():
    return api.load("word2vec-google-news-300")


class SearchEngine:
    def __init__(self, word2vec_model, documents):
        self.word2vec_model = word2vec_model
        self.documents = documents

    def get_best_documents(self, query_bag):
        candidates = []
        query_vec = self.vectorize(query_bag)

        for doc_id, doc_bag in self.documents.items():
            doc_vec = self.vectorize(doc_bag)
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
