from collections import defaultdict
import re
import nltk
from nltk.corpus import brown

from SpellChecker.dict import dictionary

# Download the Brown corpus if not already downloaded
nltk.download('brown')

PATHS = [
    "../../../resources/dictionary/english-words.10",
    "../../../resources/dictionary/english-words.20",
    "../../../resources/dictionary/english-words.35",
    "../../../resources/dictionary/english-words.40",
    "../../../resources/dictionary/english-words.50",
    "../../../resources/dictionary/english-words.55",
    # "../resources/dictionary/english-words.60",
    # "../resources/dictionary/english-words.70"
]


class BigramSpellChecker:
    def __init__(self, dictionary):
        self.bigram_model = self.build_bigram_model()
        self.dictionary = dictionary

    def get_model(self):
        return self.bigram_model

    def build_bigram_model(self):
        # Initialize a defaultdict to store bigram frequencies
        bigram_freq = defaultdict(lambda: defaultdict(int))

        # Iterate through sentences in the Brown corpus and count bigram frequencies
        for sentence in brown.sents():
            # Preprocess the sentence: lowercase, remove punctuation, and pad with <s> and </s>
            sentence = ['<s>'] + [word.lower() for word in sentence if re.match(r'^[a-zA-Z]+$', word)] + ['</s>']
            # Update bigram frequencies
            for w1, w2 in nltk.bigrams(sentence):
                bigram_freq[w1][w2] += 1

        # Convert frequencies to probabilities
        bigram_model = defaultdict(lambda: defaultdict(float))
        for w1 in bigram_freq:
            total_count = sum(bigram_freq[w1].values())
            for w2 in bigram_freq[w1]:
                bigram_model[w1][w2] = bigram_freq[w1][w2] / total_count

        return bigram_model

    def generate_candidates(self, word):
        # For simplicity, generate candidate corrections by considering only edit distance of 1
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletions = [a + b[1:] for a, b in splits if b]
        insertions = [a + c + b for a, b in splits for c in alphabet]
        substitutions = [a + c + b[1:] for a, b in splits if b for c in alphabet]
        transpositions = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]

        candidates = set(deletions + insertions + substitutions + transpositions)
        return candidates

    def spellcheck(self, word, previous_word):
        # if word.lower() in self.bigram_model:
        #     return word  # Word exists in the corpus, so it's considered correctly spelled

        candidates = self.generate_candidates(word)
        cleared_candidates = [cand for cand in candidates if self.dictionary.contains_word(cand)]
        best_candidates = sorted(cleared_candidates, key=lambda x: self.bigram_model[previous_word][x], reverse=True)

        return best_candidates


# Example usage:
dictionary.init_dict(PATHS)
spellchecker = BigramSpellChecker(dictionary)

if __name__ == '__main__':
    previous_word = 'high'
    misspelled_word = "scool"

    corrected_word = spellchecker.spellcheck(misspelled_word, previous_word)
    print(f"Original word: {misspelled_word}, Corrected word: {corrected_word}")
