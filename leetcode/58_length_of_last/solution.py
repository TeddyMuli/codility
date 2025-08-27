class Solution:
    def lengthOfLastWord(self, s):
        count = 0
        start = False

        for char in s[::-1]:
            if char == ' ':
                if start: return count
            else:
                if not start: start = True
                count += 1
        return count
if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    sol = Solution()
    print(sol.lengthOfLastWord(s))
