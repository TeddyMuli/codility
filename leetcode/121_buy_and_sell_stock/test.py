import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        test = [7,1,5,3,6,4]
        return self.assertEqual(sol.maxProfit(test), 5)
    
if __name__ == "__main__":
    unittest.main()
