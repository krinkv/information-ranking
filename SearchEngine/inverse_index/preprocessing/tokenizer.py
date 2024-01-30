from SearchEngine.inverse_index.preprocessing.stop_words import get_stop_words

CORPUS_DIR = '../../resources/'


# """
# Tokenize document content.
# :param doc: The document content presented as a string
# :return: List of tokens (terms) from document content
# """
# returns bag of words per document
def tokenize_document(doc):
    words = [word for sentence in doc for word in sentence]
    words_without_category = words[3:]
    words_to_remove = get_stop_words()
    return [word for word in words_without_category if word not in words_to_remove]
