import dict.dictionary as dictionary

PATHS = ["./resources/english-words.10",
         "./resources/english-words.20",
         "./resources/english-words.35",
         "./resources/english-words.40",
         "./resources/english-words.50",
         "./resources/english-words.55",
         "./resources/english-words.60",
         "./resources/english-words.70"]

if __name__ == '__main__':
    dictionary.init_dict(PATHS)
