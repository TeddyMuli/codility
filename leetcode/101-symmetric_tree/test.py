from solution import Solution, TreeNode
import unittest

class TestSolution(unittest.TestCase):
    def listToBt(self, arr):
        nodes = [TreeNode(val) for val in arr]
        kids = nodes[::-1]
        root = kids.pop()

        for node in nodes:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

        return root

    def test(self):
        sol = Solution()
        tests = [
            ([1,2,2,3,4,4,3], True),
            ([1,2,2,None,3,None,3], False)
        ]
        for test, expected in tests:
            with self.subTest(test=test):
                root = self.listToBt(test)
                self.assertEqual(sol.isSymmetric(root), expected)

if __name__ == "__main__":
    unittest.main()
