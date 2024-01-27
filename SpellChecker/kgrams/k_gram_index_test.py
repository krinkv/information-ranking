import unittest
from k_gram_index import get_word_k_grams


class KGramIndexTest(unittest.TestCase):
    def test_get_word_k_grams(self):
        result = get_word_k_grams('mother')
        expected_result = ['mot', 'oth', 'the', 'her']
        self.assertEqual(expected_result, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
