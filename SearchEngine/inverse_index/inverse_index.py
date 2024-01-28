
documents = None
index = None


def init_documents(paths):
    """
    Initialize the `documents` dictionary that would be:
        doc number -> doc content
    To get document content, use the `read_document` function in io-util.py
    Consider what "document content" means, i.e.:
        - raw document
        - document with preprocessed words (if we are going to store terms in normalized form). Then,
          if we want to display original document to user, just read it again.
    :param paths: a list of paths to documents
    :return: Initialized `documents`
    """
    # TODO: implement
    pass


def init_index():
    """
    Read content of all docs and preprocess it (i.e. tokenize it, remove stop words, consider form of storing words).
    Then initialize `index` dictionary that would be:
        word (or term) -> list of numbers of the docs that contain word (or term)
    :return: Initialized `index`
    """
    # TODO: implement
    pass
