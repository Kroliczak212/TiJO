import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from lottery import lottery



class TestLottery(unittest.TestCase):
    def test_elements_with_exact_repetitions(self):
        # Test dla elementów pojawiających się dokładnie określoną liczbę razy
        self.assertEqual(lottery([1, 1, 3, 2, 2, 2, 4, 5], 2), [1])
        self.assertEqual(lottery([1, 1, 2, 2, 2, 3, 4, 5], 3), [2])

    def test_multiple_elements_with_same_count(self):
        # Test dla wielu elementów z tą samą liczbą powtórzeń
        self.assertEqual(set(lottery([1, 2, 2, 2, 3, 4, 5, 5, 1], 2)), set([1, 5]))

    def test_empty_result(self):
        # Test dla braku elementów spełniających warunek
        self.assertEqual(lottery([1, 1, 2, 2, 2, 3, 4, 5], 7), [])

    def test_none_inputs(self):
        # Test dla wartości None
        self.assertEqual(lottery(None, 1), [])
        self.assertEqual(lottery([1, 2, 3], None), [])
        self.assertEqual(lottery(None, None), [])

if __name__ == '__main__':
    unittest.main()
