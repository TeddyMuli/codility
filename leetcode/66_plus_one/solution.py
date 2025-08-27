class Solution:
    def plusOne(self, digits):
        num = 0
        digits.reverse()
        for i in range(len(digits)):
            num += digits[i] * 10 ** i
        n = 0
        num += 1
        dummy = num

        while dummy > 0:
            dummy //= 10
            n += 1
        
        ans = [0] * n
        while num > 0:
            ans[n-1] = num % 10
            num //= 10
            n -= 1
        return ans

if __name__ == "__main__":
    digits = [1,2,3]
    sol = Solution()
    print(sol.plusOne(digits))
