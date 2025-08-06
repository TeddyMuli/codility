#!/usr/bin/python3
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time):
        count = 0
        remainders_map = defaultdict(int)

        for t in time:
            rem = t % 60
            compliment = (60 - rem) % 60
            count += remainders_map[compliment]
            remainders_map[rem] += 1

        return count

if __name__ == "__main__":
    sol = Solution()
    time = [30,20,150,100,40]
    print(sol.numPairsDivisibleBy60(time))
