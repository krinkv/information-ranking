index = None
k = None


def init_index(k, words):
    """
    Initialize the K-gram index with the words from the dictionary

    :param k: Gram length
    :param words: A list of all words in dictionary
    :return: Nothing I guess?
    """
    # TODO: Implement
    pass


def get_best_candidates(word):
    """
    Gets some of the best candidates for a spell correction for `word`.
    Based on Jaccard coefficient.
    To be discussed how many candidates to return.

    :param word: The word to get good candidates for
    :return: A list of the best candidate words
    """
    # TODO: Implement
    pass


def __get_common_gram_words(word):
    """
    This is meant to be a private function.

    :param word:
    :return: A list of all words that have a common K-gram with `word`
    """
    # TODO: Implement
    pass


def __get_word_k_grams(word):
    """
        This is meant to be a private function.

        :param word:
        :return: A list of all K-grams of letters of `word`
        """
    # TODO: Implement
    pass
