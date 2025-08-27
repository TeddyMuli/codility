class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 0, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(8))
