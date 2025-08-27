class Solution:
    def addBinary(self, a, b):
        return format((int(a, 2) + int(b, 2)), 'b')

if __name__ == "__main__":
    sol = Solution()
    a, b = '11', '1'
    print(sol.addBinary(a, b))
