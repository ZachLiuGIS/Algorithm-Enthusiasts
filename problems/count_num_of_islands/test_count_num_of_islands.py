import unittest
from count_num_of_islands import count_land_loop, count_land_recursive



class TwoLoopsSolutionTest(unittest.TestCase):

    def test_function(self):
        earth1 = [[1, 0, 0],
              [0, 1, 1],
              [0, 1, 0]]

        earth2 = [[1, 1, 0, 0, 0, 0],
                  [1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 1]]

        earth3 = [[1, 1, 0, 0, 1, 1],
                  [1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 1, 0, 0],
                  [1, 0, 1, 1, 0, 1]]

        earth4 = [[1, 1, 0, 0, 1, 1],
                  [1, 0, 1, 1, 0, 1],
                  [0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0]]

        earth5 = [[1, 1, 1, 0, 1, 1],
                  [1, 0, 1, 1, 1, 1],
                  [1, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 0, 1]]

        self.assertEqual(count_land_loop(earth1), 2)
        self.assertEqual(count_land_loop(earth2), 3)
        self.assertEqual(count_land_loop(earth3), 5)
        self.assertEqual(count_land_loop(earth4), 4)
        self.assertEqual(count_land_loop(earth5), 1)


class RecursionSolutiontest(unittest.TestCase):

    def test_function(self):
        earth1 = [[1, 0, 0],
              [0, 1, 1],
              [0, 1, 0]]

        earth2 = [[1, 1, 0, 0, 0, 0],
                  [1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1, 1]]

        earth3 = [[1, 1, 0, 0, 1, 1],
                  [1, 0, 1, 1, 0, 1],
                  [0, 0, 0, 1, 0, 0],
                  [1, 0, 1, 1, 0, 1]]

        earth4 = [[1, 1, 0, 0, 1, 1],
                  [1, 0, 1, 1, 0, 1],
                  [0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0]]

        earth5 = [[1, 1, 1, 0, 1, 1],
                  [1, 0, 1, 1, 1, 1],
                  [1, 0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 0, 1]]

        self.assertEqual(count_land_recursive(earth1), 2)
        self.assertEqual(count_land_recursive(earth2), 3)
        self.assertEqual(count_land_recursive(earth3), 5)
        self.assertEqual(count_land_recursive(earth4), 4)
        self.assertEqual(count_land_recursive(earth5), 1)


if __name__ == '__main__':
    unittest.main()
