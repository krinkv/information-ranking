from enum import Enum


class Popularity(Enum):
    VERY_COMMON = 10
    FAIRLY_COMMON = 20
    COMMON = 35
    UNCOMMON = 40
    FAIRLY_UNCOMMON = 50
    RARE = 55
    EPIC = 60
    LEGENDARY = 70


dictionary = {}


def init_dict(paths):
    for path in paths:
        with open(path, 'r') as file:
            file_words = [line.strip() for line in file]
            extension = path.split('.')[-1]

            for word in file_words:
                dictionary[word] = Popularity(int(extension))


def get_all_words():
    return dictionary.keys()


def contains_word(word):
    """
    Check if the given `word` is an existing one in the dictionary.

    :param word: The word to check
    :return: True if word is in dictionary, False otherwise
    """
    # TODO: Implement
    pass


def get_word_popularity(word):
    """
    Get how common `word` is
    :param word: The word to check popularity for
    :return: A value of type `Popularity` (enum constant)
    """
    # TODO: Implement
    pass
