#!/usr/bin/python3
from collections import Counter
class Solution:
    def canReorderDoubled(self, arr):
        counter = Counter(arr)

        for x in sorted(counter, key=abs):
            if counter[2*x] < counter[x]:
                return False
            counter[2*x] -=  counter[x]

        return True

if __name__ == "__main__":
    sol = Solution()
    arr = [3,1,3,6]
    print(sol.canReorderDoubled(arr))
