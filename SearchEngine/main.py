import time
from collections import Counter

from SearchEngine.inverse_index.inverse_index import init_documents_word_embeddings
from SearchEngine.inverse_index.preprocessing.tokenizer import tokenize_query
from SearchEngine.ranking.word_embeddings.search_engine import init_word2vec_model, SearchEngine
from SearchEngine.web.main_controller import app



if __name__ == '__main__':
    # app.run(debug=True)
    current_time = time.time()

    print('Loading documents...')
    documents = init_documents_word_embeddings()
    print(f'Seconds to load: {time.time() - current_time}')
    current_time = time.time()

    print('Loading word2vec model...')
    w2v_model = init_word2vec_model()
    print(f'Seconds to load: {time.time() - current_time}')

    search_engine = SearchEngine(w2v_model, documents)

    while True:
        query = input('> ')
        print(f'Best documents for query: {query}')
        current_time = time.time()
        query_bag = Counter(tokenize_query(query.lower()))
        print(search_engine.get_best_documents(query_bag))
        print(f'Seconds to process query: {time.time() - current_time}')
        current_time = time.time()

