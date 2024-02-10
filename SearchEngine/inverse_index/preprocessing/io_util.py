from SearchEngine.inverse_index.inverse_index import CORPUS_DIR


DOC_PATH = CORPUS_DIR + "/doc%d.txt"


def read_doc(doc_id):
    path = DOC_PATH % (10000 + doc_id)

    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ""
