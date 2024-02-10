"""
Implement API for communication with front-end.
"""

import time
from collections import Counter

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from SearchEngine.inverse_index.preprocessing.io_util import read_doc
from SearchEngine.inverse_index.preprocessing.tokenizer import tokenize_query
from SearchEngine.ranking.tf_idf.search_engine import init_tf_idf_engine
from SearchEngine.ranking.word_embeddings.search_engine import init_engine as init_we_engine
from SpellChecker.query.spell_checker import init_spellchecker

app = Flask(__name__)
spellchecker = init_spellchecker()
tf_idf_search_engine = init_tf_idf_engine()
# word_embedding_search_engine = init_we_engine()

CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})  # Adjust the path and origins as needed


@app.route('/api/search', methods=['POST'])
def search():
    start_time = time.time()

    data = request.get_json()
    query = data.get('query')
    algorithm = data.get('algorithm')
    if query is None:
        return jsonify(f'Invalid fields: {list(data.keys())}'), 400

    preprocessed_query = Counter(tokenize_query(query.lower()))
    try:
        if algorithm == 'tf-idf':
            result = tf_idf_search_engine.get_best_documents(preprocessed_query)
        else:
            # result = word_embedding_search_engine.get_best_documents(preprocessed_query)
            pass
    except ValueError:
        return jsonify(f'Query is empty or all words are invalid'), 400

    converted_objects = []

    for element in result:
        converted_object = {
            "doc_id": element[0],
            "title": element[1],
            "preview": element[2]
        }
        converted_objects.append(converted_object)

    print(f'Time to process query: {time.time() - start_time}')

    return jsonify(converted_objects)


@app.route('/api/spellcheck', methods=['POST'])
def spellcheck():
    data = request.get_json()
    query = data.get('query')
    if query is None:
        return jsonify(f'Invalid fields: {list(data.keys())}'), 400

    result = spellchecker.word_corrections(query)

    if len(result) == 0:
        return make_response('', 204)
    else:
        return jsonify(result)


@app.route('/api/documents/<doc_id>', methods=['GET'])
def get_document(doc_id):
    try:
        parsed_id = int(doc_id)
    except ValueError:
        return jsonify(f'Document id not an integer: {doc_id}'), 400

    if parsed_id < 0 or parsed_id > 2224:
        return jsonify(f'No document with document id: {doc_id}'), 400

    raw_doc = read_doc(parsed_id)
    return jsonify(raw_doc)
