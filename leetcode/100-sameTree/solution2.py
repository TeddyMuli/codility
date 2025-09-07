from collections import deque

class Solution:
    def sameTree(self, p, q):
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()

            if not node_p and not node_q:
                continue
            if not node_p or not node_q:
                return False
            if node_p.val != node_q.val:
                return False
            
            queue_p.append(node_p.left)
            queue_p.append(node_p.right)
            queue_q.append(node_q.left)
            queue_q.append(node_q.right)
            
        return not queue_p and not queue_q
