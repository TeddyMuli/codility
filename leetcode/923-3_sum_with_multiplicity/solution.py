#!/usr/bin/python3
from collections import Counter
class Solution(object):
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        count = 0
        counter = Counter(arr)
        keys = sorted(counter)

        for i in range(len(keys)):
            x = keys[i]
            for j in range(i, len(keys)):
                y = keys[j]
                z = target - x - y
                if z < y or z not in counter:
                    continue

                if x == y == z:
                    n = counter[x]
                    count += n * (n-1) * (n-2) // 6
                elif x == y != z:
                    n = counter[x]
                    count += (n * (n-1) // 2) * counter[z]
                elif x < y == z:
                    n = counter[y]
                    count += counter[x] * (n * (n-1) // 2)
                else:
                    if z > y and y > x:
                        count += counter[x] * counter[y] * counter[z]
                    
        return count % MOD

if __name__ == "__main__":
    sol = Solution()
    test = [1,1,2,2,3,3,4,4,5,5]
    print(sol.threeSumMulti(test, 8))
