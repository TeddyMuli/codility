class Solution:
    def maxDepthBT(self, root):
        if root is None:
            return 0
        
        maxDepthLeft = self.maxDepthBT(root.left)
        maxDepthRight = self.maxDepthBT(root.right)
        return max(maxDepthLeft, maxDepthRight) + 1
