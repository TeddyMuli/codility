from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        need = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            if counter[char] > 0:
                need -= 1
            counter[char] -= 1

            if need == 0:
                while left < right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:
                    start, end = left, right
                    
                counter[s[left]] += 1
                left += 1
                need += 1
            
        return s[start:end]
