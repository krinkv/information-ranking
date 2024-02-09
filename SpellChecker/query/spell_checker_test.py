import time

import SpellChecker.dict.dictionary as dictionary
import SpellChecker.kgrams.k_gram_index as k_gram_index
from SpellChecker.query.spell_checker import SpellChecker

from SpellChecker.util.io_util import read_testing_data

KAGGLE_TESTING_DATA_PATH = "../../resources/dictionary/kaggle-testing-data.txt"
WIKIPEDIA_TESTING_DATA_PATH = "../../resources/dictionary/wikipedia-testing-data.txt"
FILE_PATHS = [
    "../../resources/dictionary/english-words.10",
    "../../resources/dictionary/english-words.20",
    "../../resources/dictionary/english-words.35",
    "../../resources/dictionary/english-words.40",
    "../../resources/dictionary/english-words.50",
    "../../resources/dictionary/english-words.55",
    # "../../resources/dictionary/english-words.60",
    # "../../resources/dictionary/english-words.70"
]

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'


def execute_test(spell_checker, testing_dict):
    positives = 0

    print()
    start_time = time.time()

    for mistake in testing_dict.keys():
        expected = testing_dict[mistake]
        corrections = spell_checker.word_corrections(mistake)
        if len(corrections) == 0:
            continue

        actual = corrections[:3]
        actual_words = set(map(lambda tup: tup[0], actual))
        print(YELLOW + 'mistake: ' + mistake + ENDC)
        print(GREEN + 'expected: ' + expected + ENDC)

        if expected in actual_words:
            print(GREEN + 'actual: ' + str(actual) + ENDC)
            positives += 1
        else:
            print(RED + 'actual: ' + str(actual) + ENDC)

        print()

    print(f'Seconds to complete test: {time.time() - start_time}')
    accuracy = positives / len(testing_dict)
    print('Positives: ' + str(positives))
    print('All: ' + str(len(testing_dict)))
    print('Accuracy: ' + str(accuracy))


def test_word_corrections():
    dictionary.init_dict(FILE_PATHS)
    file_words = dictionary.get_all_words()
    k_gram_index.init_index(file_words)

    spell_checker = SpellChecker(k_gram_index, dictionary)
    kaggle_testing_dict = read_testing_data(KAGGLE_TESTING_DATA_PATH)
    wikipedia_testing_dict = read_testing_data(WIKIPEDIA_TESTING_DATA_PATH)

    print('\n------------------------Kaggle testing dataset----------------------------------------\n')
    execute_test(spell_checker, kaggle_testing_dict)
    print('\n------------------------Wikipedia testing dataset----------------------------------------\n')
    execute_test(spell_checker, wikipedia_testing_dict)


if __name__ == '__main__':
    test_word_corrections()

