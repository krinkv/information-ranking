import numpy as np


class SearchEngine:
    def __init__(self, dictionary, documents, index):
        self.dictionary = dictionary
        self.documents = documents
        self.index = index

    def get_best_documents(self, query):
        candidates = [(doc_id, doc_content) for doc_id, doc_content in self.documents]

        vec_query = self.vectorize(query)
        vec_candidates = list(
            map(lambda pair: (pair[0], self.vectorize(pair[1])), candidates)
        )

        sorted_candidates = sorted(vec_candidates,
                                   key=lambda v_c: self.cosine_similarity(vec_query, v_c[1]),
                                   reverse=True)

        return [pair[0] for pair in sorted_candidates][:10]

    def tf_idf(self, term, bag):
        return self.tf(term, bag) * self.idf(term)

    def tf(self, term, bag):
        return sum([1 if term == word else 0 for word in bag])

    def idf(self, term):
        docs_content = self.documents.values()
        df = sum([1 if term in doc else 0 for doc in docs_content])

        return np.log(len(self.documents) / df)

    def vectorize(self, bag):
        bag_vec = np.zeros(len(self.dictionary))

        for term in bag:
            tf_idf_value = self.tf_idf(term, bag)
            try:
                index = self.dictionary.index(term)
                bag_vec[index] = tf_idf_value
            except ValueError:
                pass

        return bag_vec

    def cosine_similarity(self, query_vec, doc_vec):
        dot_product = np.dot(query_vec, doc_vec)
        norm_q = np.linalg.norm(query_vec)
        norm_d = np.linalg.norm(doc_vec)
        return dot_product / (norm_q * norm_d)
