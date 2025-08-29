import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ([2, 1, 1, 2, 1, 2, 2], 2),
            ([3,2,3], 3),
            ([4], 4)
        ]
        for data, expected in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.majorityElement(data), expected)

if __name__ == "__main__":
    unittest.main()
