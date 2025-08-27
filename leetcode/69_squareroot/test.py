import unittest
from solution_1 import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            (0, 0),
            (1, 1),
            (4, 2),
            (8, 2),
            (10, 3),
            (100, 10)
        ]
        for data, expected in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.mySqrt(data), expected)

if __name__ == "__main__":
    unittest.main()
