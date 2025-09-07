import unittest
from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSolution(unittest.TestCase):
    def listToBt(self, arr):
        if not arr:
            return None
        
        nodes = [TreeNode(val) if val else None for val in arr]
        kids = nodes[::-1]
        root  = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()

        return root

    def test(self):
        sol = Solution()
        tests = [
            ([3,9,20,None,None,15,7], 3),
            ([1,None,2], 2)
        ]
        for test, expected in tests:
            with self.subTest(test):
                root = self.listToBt(test)
                self.assertEqual(sol.maxDepthBT(root), expected)
    
if __name__ == "__main__":
    unittest.main()
