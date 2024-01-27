import Levenshtein

from SpellChecker.dict.dictionary import Popularity

WORD_WEIGHTS = {
    Popularity.VERY_COMMON.name: 0.7,
    Popularity.FAIRLY_COMMON.name: 0.6,
    Popularity.COMMON.name: 0.5,
    Popularity.UNCOMMON.name: 0.4,
    Popularity.FAIRLY_UNCOMMON.name: 0.3,
    Popularity.RARE.name: 0.2,
    Popularity.EPIC.name: 0.15,
    Popularity.LEGENDARY.name: 0.1
}


class SpellChecker:
    def __init__(self, k_gram_index, dictionary):
        self.k_gram_index = k_gram_index
        self.dictionary = dictionary

    def word_corrections(self, input_word):
        k_gram_candidates = [tuple_candidate[0] for tuple_candidate in
                             self.k_gram_index.get_best_candidates(input_word)]

        similarities = [
            (word, Levenshtein.distance(input_word, word)
             * WORD_WEIGHTS.get(self.dictionary.get_word_popularity(word).name))
            for word in k_gram_candidates
        ]
        return sorted(similarities, key=lambda x: x[1])[:3]

