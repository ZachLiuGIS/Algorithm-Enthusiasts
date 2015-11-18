import unittest
from str_permutation import str_permutation


class StringPermutationTest(unittest.TestCase):

    def test_str_permutation(self):
        s = 'abc'
        self.assertEquals = (str_permutation(s), [
            'abc', 'abc', 'bac', 'bca', 'cab', 'cba'
        ])
