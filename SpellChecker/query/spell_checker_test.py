import SpellChecker.dict.dictionary as dictionary
import SpellChecker.kgrams.k_gram_index as k_gram_index
from SpellChecker.query.spell_checker import SpellChecker

from SpellChecker.util.io_util import read_testing_data

TESTING_DATA_PATH = "../../resources/dictionary/testing-data.txt"
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


def test_word_corrections():
    dictionary.init_dict(FILE_PATHS)
    file_words = dictionary.get_all_words()
    k_gram_index.init_index(file_words)

    spell_checker = SpellChecker(k_gram_index, dictionary)
    testing_dict = read_testing_data(TESTING_DATA_PATH)
    positives = 0

    print()
    for mistake in testing_dict.keys():
        expected = testing_dict[mistake]
        corrections = spell_checker.word_corrections(mistake)
        if len(corrections) == 0:
            continue

        actual = corrections[0][0]
        print(YELLOW + 'mistake: ' + mistake + ENDC)
        print(GREEN + 'expected: ' + expected + ENDC)

        if expected == actual:
            print(GREEN + 'actual: ' + actual + ENDC)
            positives += 1
        else:
            print(RED + 'actual: ' + actual + ENDC)

        print()
    accuracy = positives / len(testing_dict)
    print('Positives: ' + str(positives))
    print('All: ' + str(len(testing_dict)))
    print('Accuracy: ' + str(accuracy))


if __name__ == '__main__':
    test_word_corrections()
