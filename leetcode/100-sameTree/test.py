import unittest
from solution import Solution

class BinaryTree:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

class TestSolution(unittest.TestCase):
    def listToBt(self, arr):
        nodes = [BinaryTree(val) for val in arr]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()

        return root

    def test(self):
        tests = [
            ([1,2,3], [1,2,3], True),
            ([1,2], [1,None,2], False)
        ]
        sol = Solution()
        for p, q, expected in tests:
            with self.subTest(data=(p,q)):
                p = self.listToBt(p)
                q = self.listToBt(q)
                self.assertEqual(sol.sameTree(p, q), expected)

if __name__ == "__main__":
    unittest.main()
