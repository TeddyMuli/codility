import unittest
from solution import Solution
class TestSolution(unittest.TestCase):
    def test(self):
        test = [1,2,3,4,5,6,7]
        sol = Solution()
        sol.rotateArray(test, 3)
        return self.assertEqual(test, [5,6,7,1,2,3,4])
    
if __name__ == "__main__":
    unittest.main()
