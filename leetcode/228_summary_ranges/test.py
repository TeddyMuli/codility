import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ([0,1,2,4,5,7], ["0->2","4->5","7"]),
            ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
            ([], []),
            ([-1000, 0, 100, 10000, 123487, 123488], ["-1000","0","100","10000","123487->123488"])
        ]
        for test, expected in tests:
            with self.subTest(test=test):
                self.assertEqual(sol.summaryRanges(test), expected)

if __name__ == "__main__":
    unittest.main()
