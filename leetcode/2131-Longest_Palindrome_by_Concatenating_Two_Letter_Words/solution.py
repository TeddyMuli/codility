#!/usr/bin/python3
from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, words):
        m = defaultdict(int)
        unpaired = count = 0

        for word in words:
            if word[0] == word[1]:
                if m[word] > 0:
                    unpaired -= 1
                    m[word] -= 1
                    count += 4
                else:
                    unpaired += 1
                    m[word] += 1
            else:
                if m[word[::-1]] > 0:
                    count += 4
                    m[word[::-1]] -= 1
                else:
                    m[word] += 1
            
        if unpaired > 0: count += 2
        return count
        
if __name__ == "__main__":
    sol = Solution()
    words = ["lc","cl","gg"]
    #words =["ab","ty","yt","lc","cl","ab"]
    #words = ["cc","ll","xx"]
    print(sol.longestPalindrome(words))
