"""
Implement API for communication with front-end.
"""

import time
from collections import Counter

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from SearchEngine.inverse_index.preprocessing.tokenizer import tokenize_query
from SearchEngine.ranking.search_engine import init_engine
from SpellChecker.query.spell_checker import init_spellchecker

app = Flask(__name__)
search_engine = init_engine()
spellchecker = init_spellchecker()

CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})  # Adjust the path and origins as needed


@app.route('/api/search', methods=['POST'])
def search():
    start_time = time.time()

    data = request.get_json()
    query = data.get('query')
    if query is None:
        return jsonify(f'Invalid fields: {list(data.keys())}'), 400

    preprocessed_query = Counter(tokenize_query(query.lower()))
    result = search_engine.get_best_documents(preprocessed_query)

    print(f'Time to process query: {time.time() - start_time}')

    return jsonify(result)


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
