from SearchEngine.web.main_controller import app


if __name__ == '__main__':
    app.run(debug=False)
    # current_time = time.time()
    #
    # print('Loading documents...')
    # documents = init_documents_word_embeddings()
    # print(f'Seconds to load: {time.time() - current_time}')
    # current_time = time.time()
    #
    # print('Loading word2vec model...')
    # w2v_model = init_word2vec_model()
    # print(f'Seconds to load: {time.time() - current_time}')
    # current_time = time.time()
    #
    # print('Vectorizing documents...')
    # search_engine = SearchEngine(w2v_model, documents)
    # print(f'Seconds to vectorize: {time.time() - current_time}')
    # current_time = time.time()
    #
    # while True:
    #     query = input('> ')
    #
    #     if query.strip() == 'exit':
    #         break
    #
    #     print(f'Best documents for query: {query}')
    #     query_bag = Counter(tokenize_query(query.lower()))
    #     print(search_engine.get_best_documents(query_bag))
    #     print(f'Seconds to process query: {time.time() - current_time}')
    #     current_time = time.time()

