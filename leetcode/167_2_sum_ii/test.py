import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        tests = [
            ([2,7,11,15], [1,2], 9),
            ([2,3,4], [1,3], 6),
            ([-1,0], [1,2], -1)
        ]
        sol = Solution()
        for data, expected, target in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.twoSum(data, target), expected)

if __name__ == "__main__":
    unittest.main()
