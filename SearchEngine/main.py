import time

from SearchEngine.inverse_index.inverse_index import init_documents, init_index
from SearchEngine.inverse_index.preprocessing.stop_words import init_stop_words
import SpellChecker.dict.dictionary as dictionary
from SearchEngine.ranking.search_engine import SearchEngine
from SearchEngine.user_interaction.user_interaction import user_interactive_loop
from SpellChecker.main import PATHS


def init_engine():
    start_time = time.time()

    dictionary.init_dict(PATHS)
    dictionary_words = dictionary.get_all_words()
    init_stop_words()
    documents = init_documents()
    index = init_index()

    engine = SearchEngine(dictionary_words, documents, index)
    print(f'Time to initialize engine: {time.time() - start_time}')

    return engine


if __name__ == '__main__':
    search_engine = init_engine()
    user_interactive_loop(search_engine)

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
