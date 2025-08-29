import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        tests = [
            ([1], 1),
            ([1,1,1], 3),
            ([1,2,3], 6),
            ([1,2,2], 4),
            ([4,3,2,1], 10),
            ([1,2,2,4], 6),
            ([4,2,1,1], 7),
            ([1,2,3,5,2], 11)
        ]

        for data, expected in tests:
            with self.subTest(data=data):
                self.assertEqual(sol.candy(data), expected)

if __name__ == "__main__":
    unittest.main()
