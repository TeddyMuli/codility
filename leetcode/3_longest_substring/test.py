import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3)
        ]

        for test, expected in tests:
            with self.subTest(test=test):
                self.assertEqual(sol.lengthOfLongestSubstring(test), expected)

if __name__ == "__main__":
    unittest.main()
