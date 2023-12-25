# word weights based on popularity
# Should be a hash table that looks like this:
# Popularity -> float
word_weights = None


def word_corrections(word):
    """
    Get a list of the best corrections of `word`
    Idea is to find candidates with K-gram index and then calculate edit distance on them with `word`.
    Along with the edit distance, take into account the weight of the word (its popularity).
    To be discussed how many corrections to return.

    :param word: The word to get corrected
    :return: A list of the best corrections for `word`
    """
    # TODO: Implement
    pass
