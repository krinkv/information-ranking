from SearchEngine.web.main_controller import app


if __name__ == '__main__':
    app.run(debug=True)

    # print(search_engine.get_best_documents('transfer from chelsea to leeds'))

    # start_time = time.time()
    # for i in range(10):
    #     search_engine.vectorize(documents[i])
    #     curr_time = time.time()
    #     print(f'Elapsed time on {i + 1}th doc vectorization: {curr_time - start_time} seconds')
    #
    # print()
    #
    # start_time = time.time()
    # term = 'health'
    # doc_ids = list(index[term])[:10]
    # for i in range(10):
    #     search_engine.tf_idf(term, documents[doc_ids[i]])
    #     curr_time = time.time()
    #     print(f'Elapsed time on {i + 1}th tf-idf: {curr_time - start_time} seconds')
    #
    # print()
    #
    # start_time = time.time()
    # terms = ['health', 'sport', 'people', 'willing', 'hedgehog',
    #          'reliability', 'pen', 'concurrent', 'abruption', 'morphinism']
    # for i in range(10):
    #     dictionary_words.index(terms[i])
    #     curr_time = time.time()
    #     print(f'Elapsed time on {i + 1}th dictionary index search: {curr_time - start_time} seconds')
    #
    # print('aaa')
