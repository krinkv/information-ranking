from SearchEngine.inverse_index.inverse_index import init_documents, init_index
from SearchEngine.inverse_index.preprocessing.stop_words import init_stop_words
import SpellChecker.dict.dictionary as dictionary
from SearchEngine.ranking.search_engine import SearchEngine
from SpellChecker.main import PATHS
from SpellChecker.util.io_util import read_file_lines


def user_interactive_loop():
    # TODO: implement
    pass


def add_numbers_to_corp_files():
    path = '../resources/corpus.txt'
    lines = read_file_lines(path)

    with open(path, 'w') as file:
        for i in range(len(lines)):
            file.write(lines[i])
            file.write('\n\n')


if __name__ == '__main__':
    dictionary.init_dict(PATHS)
    dictionary_words = dictionary.get_all_words()

    init_stop_words()
    documents = init_documents()
    index = init_index()

    search_engine = SearchEngine(dictionary_words, documents, index)
    print("aaa")
    print("uuu")
