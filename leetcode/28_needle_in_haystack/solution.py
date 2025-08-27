class Solution:
    def strStr(self, haystack, needle):
        if not needle or len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    haystack = "aduyiouisad"
    needle = "sad"
    sol = Solution()
    print(sol.strStr(haystack, needle))
