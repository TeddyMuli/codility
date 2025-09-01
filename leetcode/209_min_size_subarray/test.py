import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ([2,3,1,2,4,3], 7, 2),
            ([1,4,4], 4, 1),
            ([1,1,1,1,1,1,1,1], 11, 0)
        ]
        for data, target, expected in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.minSubArrayLen(target, data), expected)

if __name__ == "__main__":
    unittest.main()
