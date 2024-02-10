from collections import Counter
from enum import Enum

import pandas as pd
import xml.etree.ElementTree as ET

from SearchEngine.inverse_index.inverse_index import init_index

from SearchEngine.inverse_index.preprocessing.tokenizer import preprocess_document, tokenize_query
from SearchEngine.ranking.tf_idf.search_engine import SearchEngine as TfIdfSearchEngine
from SearchEngine.ranking.word_embeddings.search_engine import init_word2vec_model, SearchEngine as WeSearchEngine

DOCUMENTS_PATH = "../../../resources/trec/cran.all.1400.xml"
QUERIES_PATH = "../../../resources/trec/cran.qry.xml"
TREC_PATH = "../../../resources/trec/cranqrel.trec.txt"

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'


class Model(Enum):
    TF_IDF = 0
    WORD_EMBEDDINGS = 1


def load_documents():
    tree = ET.parse(DOCUMENTS_PATH)
    root = tree.getroot()
    documents = {}

    for doc in root.findall('doc'):
        docno = doc.find('docno').text
        title = doc.find('title').text
        text = doc.find('text').text

        if docno is None or title is None or text is None:
            continue

        content = "dummy " + title + " " + text
        documents[int(docno)] = preprocess_document(content.split())

    return documents


def load_queries(model):
    tree = ET.parse(QUERIES_PATH)
    root = tree.getroot()

    queries = {}

    for query in root.findall('top'):
        qryno = query.find('num').text
        qrytitle = query.find('title').text

        if qryno is None or qrytitle is None:
            continue

        queries[int(qryno)] = tokenize_query(qrytitle)

    return queries


def load_trec_data():
    with open(TREC_PATH, 'r') as file:
        file_lines = [line.strip() for line in file if len(line.strip()) > 0]

    trec_data = [(splitted[0], splitted[2], splitted[3])
                 for splitted in (line.split() for line in file_lines)]

    return pd.DataFrame(trec_data, columns=['qryno', 'docno', 'relevancy'])


def execute_test(search_engine, model):
    queries = load_queries(model)
    df = load_trec_data()
    print(df)
    positives = 0

    for qryno, query_list in queries.items():
        query_bag = Counter(query_list)
        search_result = [t[0] for t in search_engine.get_best_documents(query_bag)]

        df_relevant = df[(df['qryno'] == str(qryno)) & (df['relevancy'] == '1')]
        df_irrelevant = df[(df['qryno'] == str(qryno)) & (df['relevancy'] == '0')]

        relevant_docs = set(df_relevant['docno'])
        irrelevant_docs = set(df_irrelevant['docno'])

        best_docs = search_result \
            if len(relevant_docs) >= len(search_result) \
            else search_result[:len(search_result)]

        for doc_id in best_docs:
            if str(doc_id) in relevant_docs:
                print(GREEN + 'query: ' + str(qryno) + ", document: " + str(doc_id)
                      + ', relevancy: 1' + ', result: 1' + ENDC)
                positives += 1
            else:
                print(RED + 'query: ' + str(qryno) + ", document: " + str(doc_id)
                      + ', relevancy: 1' + ', result: 0' + ENDC)

        for docno in irrelevant_docs:
            if int(docno) not in best_docs:
                print(GREEN + 'query: ' + str(qryno) + ", document: " + str(docno)
                      + ', relevancy: 0' + ', result: 1' + ENDC)
                positives += 1
            else:
                print(RED + 'query: ' + str(qryno) + ", document: " + str(docno)
                      + ', relevancy: 0' + ', result: 1' + ENDC)

    accuracy = positives / df.shape[0]
    print(f'Positives: {positives}')
    print(f'All: {df.shape[0]}')
    print(f'Accuracy: {accuracy}')


def test_get_best_documents_tf_idf():
    print("\n------------------- TF-IDF search engine -----------------------------\n")
    docs = load_documents()
    tf_idf_docs = {}

    for doc_id, doc_content in docs.items():
        tf_idf_docs[doc_id] = Counter(doc_content)

    index = init_index(tf_idf_docs)
    engine = TfIdfSearchEngine(tf_idf_docs, index)

    execute_test(engine, Model.TF_IDF)


def test_get_best_documents_word_embeddings():
    print("\n------------------- Word Embeddings search engine -----------------------------\n")
    we_docs = load_documents()
    w2v_model = init_word2vec_model()
    engine = WeSearchEngine(w2v_model, we_docs)

    execute_test(engine, Model.WORD_EMBEDDINGS)


if __name__ == '__main__':
    test_get_best_documents_tf_idf()
    test_get_best_documents_word_embeddings()
