import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 8),
            (6, 13),
            (7, 21)
        ]
        for data, expected in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.climbStairs(data), expected)

if __name__ == "__main__":
    unittest.main()
