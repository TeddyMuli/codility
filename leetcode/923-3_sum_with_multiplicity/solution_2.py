#!/usr/bin/python3
import collections, itertools
class Solution:
    def threeSumMulti(self, arr, target):
        count = 0
        MOD = 10 ** 9 + 7
        counter = collections.Counter(arr)

        for i, j in itertools.combinations_with_replacement(counter, 2):
            k = target - i - j

            if i == j ==k: count += counter[i] * (counter[i]-1) * (counter[i]-2) / 6
            elif i == j != k: count += counter[i] * (counter[i]-1) / 2 * counter[k]
            elif k > i and k > j: count += counter[i] * counter[j] * counter[k]

        return count % MOD

if __name__ == "__main__":
    sol = Solution()
    test = [1,1,2,2,3,3,4,4,5,5]
    print(sol.threeSumMulti(test, 8))
