import SpellChecker.dict.dictionary as dictionary
import SpellChecker.kgrams.k_gram_index as k_gram_index
from SpellChecker.query.spell_checker import SpellChecker

PATHS = ["../resources/english-words.10",
         "../resources/english-words.20",
         "../resources/english-words.35",
         "../resources/english-words.40",
         "../resources/english-words.50",
         "../resources/english-words.55",
         "../resources/english-words.60",
         "../resources/english-words.70"]

if __name__ == '__main__':
    dictionary.init_dict(PATHS)

    file_words = dictionary.get_all_words()
    k_gram_index.init_index(file_words)

    candidates = k_gram_index.get_best_candidates('planr')
    print('Jaccard based candidates')
    print(candidates)

    spellchecker = SpellChecker(k_gram_index, dictionary)
    print('\n\n\n')
    print('With Levenshtein distance')
    print(spellchecker.word_corrections('planr'))
