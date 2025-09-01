class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        s_set = set()

        for i in range(len(s)):
            while s[i] in s_set:
                s_set.remove(s[left])
                left += 1
            s_set.add(s[i])
            max_len = max(max_len, i - left + 1)

        return max_len
