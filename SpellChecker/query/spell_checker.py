import Levenshtein

from SpellChecker.dict import dictionary
from SpellChecker.dict.dictionary import Popularity
from SpellChecker.kgrams import k_gram_index

# approximate layout of keys and their distance on a keyboard
KEYBOARD_LAYOUT = {
    'q': (0, 0), 'w': (1, 0), 'e': (2, 0), 'r': (3, 0), 't': (4, 0), 'y': (5, 0),
    'u': (6, 0), 'i': (7, 0), 'o': (8, 0), 'p': (9, 0),

    'a': (1, 0.3), 's': (1, 1.3), 'd': (1, 2.3), 'f': (1, 3.3), 'g': (1, 4.3),
    'h': (1, 5.3), 'j': (1, 6.3), 'k': (1, 7.3), 'l': (1, 8.3), '\'': (1, 10.3),

    'z': (2, 0.7), 'x': (2, 1.7), 'c': (2, 2.7), 'v': (2, 3.7), 'b': (2, 4.7),
    'n': (2, 5.7), 'm': (2, 6.7),

    '_': (-1, 10), '-': (-1, 10)
}

POPULARITY_WEIGHTS = {}

PATHS = [
    "../resources/dictionary/english-words.10",
    "../resources/dictionary/english-words.20",
    "../resources/dictionary/english-words.35",
    "../resources/dictionary/english-words.40",
    "../resources/dictionary/english-words.50",
    "../resources/dictionary/english-words.55",
    # "../resources/dictionary/english-words.60",
    # "../resources/dictionary/english-words.70"
]


def init_spellchecker():
    dictionary.init_dict(PATHS)

    file_words = dictionary.get_all_words()
    k_gram_index.init_index(file_words)

    spellchecker = SpellChecker(k_gram_index, dictionary)
    return spellchecker


def assign_popularity_weights():
    popularities = list(Popularity)

    for popularity in popularities:
        POPULARITY_WEIGHTS[popularity.name] = popularity.value / 100


def letter_keyboard_distance(letter1, letter2):
    x1, y1 = KEYBOARD_LAYOUT[letter1]
    x2, y2 = KEYBOARD_LAYOUT[letter2]

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def word_keyboard_distance(word1, word2):
    distance = 0
    for l1, l2 in list(zip(word1, word2)):
        distance += letter_keyboard_distance(l1, l2)

    return distance / 10000


class SpellChecker:
    def __init__(self, k_gram_index, dictionary):
        self.k_gram_index = k_gram_index
        self.dictionary = dictionary
        assign_popularity_weights()

    def word_corrections(self, input_word):
        if self.dictionary.contains_word(input_word):
            return []

        k_gram_based_candidates = [tuple_candidate[0] for tuple_candidate in
                                   self.k_gram_index.get_best_candidates(input_word)]

        similarities = [
            (word,
             Levenshtein.distance(input_word, word)
             + POPULARITY_WEIGHTS[self.dictionary.get_word_popularity(word).name]
             + word_keyboard_distance(input_word, word))
            for word in k_gram_based_candidates
        ]

        return sorted(similarities, key=lambda x: x[1])[:3]
