from enum import Enum


class Popularity(Enum):
    """
    Define all values for enum that show how common a word is in the English language
    Idea is to use a words popularity to modify its 'weight' in calculations
    """


dictionary = None


def init_dict(paths):
    """
    Initialize the dictionary, which is a hash table that looks like this:
    word -> file from which the word is

    :param paths: A list of paths to files from which to load the words
    :return: Nothing I guess?
    """
    # TODO: Implement
    pass


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
