import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ("race car", True),
            ("race a car", False),
            (" ", True),
            ("A man, a plan, a canal: Panama", True)
        ]
        for data, expected in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.isPalindrome(data), expected)

if __name__ == "__main__":
    unittest.main()
