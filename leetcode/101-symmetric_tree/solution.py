from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isSame(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return False
            if not a or not b:
                return True
            return (
                a.val == b.val and
                isSame(a.left, b.right) and
                isSame(a.right, b.left)
            )
        
        return isSame(root.left, root.right)
