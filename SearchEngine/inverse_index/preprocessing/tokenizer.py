from SearchEngine.inverse_index.preprocessing.stop_words import get_stop_words

CORPUS_DIR = '../../resources/'


# """
# Preprocess document content.
# :param words: The document content presented as a list of words
# :return: List of tokens (terms) with cleared document content
# """
def preprocess_document(words):
    words_without_category = words[1:]
    words_to_remove = get_stop_words()
    return [word for word in words_without_category if word not in words_to_remove and word.isalnum()]


def tokenize_query(query):
    words = query.strip().split()
    words_to_remove = get_stop_words()
    return [word for word in words if word not in words_to_remove]
