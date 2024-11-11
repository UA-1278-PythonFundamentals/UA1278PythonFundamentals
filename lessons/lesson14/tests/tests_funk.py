import unittest
from funk import solver

class TestSolver(unittest.TestCase):


    # def test_not_solved(self):
    #     actual = solver(1, 0, 1)
    #     self.assertEqual(actual, "Дискримінант: -4 \n Рівняння розв'язків немає")

    # def test_not_solved_2(self):
    #     actual = solver(1, 1, 1)
    #     self.assertEqual(actual, "Дискримінант: -3 \n Рівняння розв'язків немає")

    # def test_solved(self):
    #     actual = solver(1, 8, 1)
    #     self.assertEqual(actual, "Дискримінант: 60 \n x1 = -0.12701665379258298 \n x2 = -7.872983346207417 \n")
    def test_solved_1(self):
        actual = solver(1, 2, 1)
        self.assertEqual(actual, "Дискримінант: 0 \n x = -1.0\n")


if __name__ == '__main__':
    unittest.main()