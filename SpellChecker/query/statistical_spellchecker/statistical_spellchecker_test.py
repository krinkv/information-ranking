import time
import re

from collections import Counter

from SpellChecker.query.statistical_spellchecker.statistical_spellchecker import correction
from SpellChecker.util.io_util import read_testing_data

KAGGLE_TESTING_DATA_PATH = "../../../resources/dictionary/kaggle-testing-data.txt"
WIKIPEDIA_TESTING_DATA_PATH = "../../../resources/dictionary/wikipedia-testing-data.txt"


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'


def execute_test(testing_dict):
    positives = 0

    print()
    start_time = time.time()

    for mistake in testing_dict.keys():
        expected = testing_dict[mistake]
        corrections = correction(mistake)
        if len(corrections) == 0:
            continue

        actual = corrections[:3]
        print(YELLOW + 'mistake: ' + mistake + ENDC)
        print(GREEN + 'expected: ' + expected + ENDC)

        if expected in corrections:
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
    kaggle_testing_dict = read_testing_data(KAGGLE_TESTING_DATA_PATH)
    wikipedia_testing_dict = read_testing_data(WIKIPEDIA_TESTING_DATA_PATH)

    print('\n------------------------Kaggle testing dataset----------------------------------------\n')
    execute_test(kaggle_testing_dict)
    print('\n------------------------Wikipedia testing dataset----------------------------------------\n')
    execute_test(wikipedia_testing_dict)


if __name__ == '__main__':
    test_word_corrections()

