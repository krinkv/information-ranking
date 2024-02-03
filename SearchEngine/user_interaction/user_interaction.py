from collections import Counter
import time

from SearchEngine.inverse_index.preprocessing.tokenizer import tokenize_query


def user_interactive_loop(search_engine):
    while True:
        # TODO: instead of taking input from console, take request from controller
        print('Type bellow what you want to search for:')
        query = input('> ')

        if query.strip() == 'exit':
            break

        start_time = time.time()
        preprocessed_query = Counter(tokenize_query(query.lower()))

        result = search_engine.get_best_documents(preprocessed_query)
        print(f'Time to process query: {time.time() - start_time}')
        # TODO: instead of printing on console, return result as a response to controller
        print(f'Result: {result}')
        print(f'\n')
