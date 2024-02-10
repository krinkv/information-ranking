import numpy as np

from SearchEngine.inverse_index.inverse_index import init_documents_tf_idf, init_index
from SearchEngine.inverse_index.preprocessing.io_util import read_doc
from SearchEngine.inverse_index.preprocessing.stop_words import init_stop_words


def init_tf_idf_engine():
    documents = init_documents_tf_idf()
    index = init_index(documents)
    init_stop_words()

    return SearchEngine(documents, index)


class SearchEngine:
    def __init__(self, documents, index):
        self.documents = documents
        self.index = index

    def get_best_documents(self, query_bag):
        candidates = []

        relevant_docs_per_query = self.get_relevant_documents(query_bag)
        for doc_id in relevant_docs_per_query:
            doc_bag = self.documents[doc_id]
            keys_intersection = self.keys_intersection(query_bag, doc_bag)
            query_vec = self.vectorize(query_bag)
            doc_vec = self.vectorize(doc_bag)
            candidates.append((doc_id, self.cosine_similarity(query_vec, doc_vec, keys_intersection)))

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

    def tf_idf(self, term, bag):
        return self.tf(term, bag) * self.idf(term)

    def tf(self, term, bag):
        return bag[term]

    def idf(self, term):
        df = len(self.index[term])

        return np.log(len(self.documents) / df) if df > 0 else 0

    def vectorize(self, bag):
        bag_vec = {}

        for term in bag:
            try:
                tf_idf_value = self.tf_idf(term, bag)
                bag_vec[term] = tf_idf_value
            except KeyError:
                bag_vec[term] = 0

        return bag_vec

    def cosine_similarity(self, query_vec, doc_vec, keys_intersection):
        dot_product = sum([query_vec[key] * doc_vec[key] for key in keys_intersection])
        norm_q = np.linalg.norm(list(query_vec.values()))
        norm_d = np.linalg.norm(list(doc_vec.values()))
        if norm_d > 0 and norm_q > 0:
            return dot_product / (norm_q * norm_d)
        else:
            return 0

    def keys_intersection(self, query, doc):
        query_keys = set(query.keys())
        doc_keys = set(doc.keys())
        return doc_keys.intersection(query_keys)

    def get_relevant_documents(self, query):
        query_keys = set(query.keys())
        relevant_doc_ids = set()
        for word in query_keys:
            if word in self.index:
                relevant_doc_ids.update(self.index[word])

        return relevant_doc_ids
