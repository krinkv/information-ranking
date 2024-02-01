import time

from SearchEngine.inverse_index.inverse_index import init_documents, init_index
from SearchEngine.inverse_index.preprocessing.stop_words import init_stop_words
import SpellChecker.dict.dictionary as dictionary
from SearchEngine.ranking.search_engine import SearchEngine
from SpellChecker.main import PATHS


def user_interactive_loop():
    # TODO: implement
    pass


if __name__ == '__main__':
    start_time = time.time()
    print(f'Start time: {start_time}')

    dictionary.init_dict(PATHS)
    dictionary_words = dictionary.get_all_words()

    init_stop_words()
    documents = init_documents()
    index = init_index()

    search_engine = SearchEngine(dictionary_words, documents, index)

    print(f'Elapsed time: {time.time() - start_time}')

    print(search_engine.get_best_documents('transfer from chelsea to leeds'))

    print(f'Elapsed time: {time.time() - start_time}')

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
