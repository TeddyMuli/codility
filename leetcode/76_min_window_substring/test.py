import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        s = "ADOBECODEBANC"
        t = "AABC"
        expected = "BANC"

        sol = Solution()
        return self.assertEqual(sol.minWindow(s, t), expected)
    
if __name__ == "__main__":
    unittest.main()
