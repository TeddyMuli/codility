class Solution:
    def climbStairs(self, n):
        if n < 3:
            return n

        prev, curr = 1, 2
        for i in range(3, n+1):
            curr += prev
            prev = curr - prev

        return curr
