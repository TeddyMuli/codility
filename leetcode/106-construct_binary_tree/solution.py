from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int] | deque[int]) -> Optional[TreeNode]:
        postorder = deque(postorder)

        def build(inorder, postorder):
            if inorder:
                idx = postorder.pop()
                root = TreeNode(inorder[idx])

                root.right = build(inorder[idx+1:], postorder)
                root.left = build(inorder[:idx], postorder)

                return root
        
        return build(inorder, postorder)
