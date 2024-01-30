from enum import Enum

from SpellChecker.util.io_util import read_file_lines


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


def clean_words(words):
    clean = []

    for word in words:
        flag = True
        for char in word:
            if not ('a' <= char <= 'z') and char != '\'':
                flag = False
                break
        if flag:
            clean.append(word)

    return clean


def init_dict(paths):
    for path in paths:
        file_words = clean_words(read_file_lines(path))
        extension = path.split('.')[-1]

        for word in file_words:
            dictionary[word] = Popularity(int(extension))


def get_all_words():
    return list(dictionary.keys())


def contains_word(word):
    return word in dictionary


def get_word_popularity(word):
    return dictionary[word]
