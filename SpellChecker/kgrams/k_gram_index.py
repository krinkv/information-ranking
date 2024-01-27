k_gram_index = {}
k = 3


def init_index(words):
    for word in words:
        # Generate k-grams for the current word
        kgrams = get_word_k_grams(word)

        # Update the index with the current word for each k-gram
        for kgram in kgrams:
            if kgram in k_gram_index:
                k_gram_index[kgram].append(word)
            else:
                k_gram_index[kgram] = [word]


def get_best_candidates(input_word):
    candidate_words = get_common_gram_words(input_word)

    similarities = [(word, jaccard_similarity(input_word, word)) for word in candidate_words]
    sorted_candidates = sorted(similarities, key=lambda x: x[1], reverse=True)
    best_candidates = [(word, similarity) for word, similarity in sorted_candidates if similarity >= 0.25][:50]
    return best_candidates


def jaccard_similarity(word1, word2):
    set1 = set(get_word_k_grams(word1))
    set2 = set(get_word_k_grams(word2))
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0


def get_common_gram_words(input_word):
    input_kgrams = get_word_k_grams(input_word)  # Adjust k for your use case

    candidate_words = set()

    for kgram in input_kgrams:
        if kgram in k_gram_index:
            candidate_words.update(k_gram_index[kgram])

    return candidate_words


def get_word_k_grams(word):
    kgrams = [word[i:i + k] for i in range(len(word) - k + 1)]

    return kgrams