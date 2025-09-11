"""
This solution uses a hashmap approach
"""
from typing import List
from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counter = Counter(nums)
        res = []
        n = len(nums)

        for i in range(n):
            counter[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                counter[nums[j]] -= 1
                k = -(nums[i] + nums[j])
                if counter[k] > 0:
                    res.append([nums[i], nums[j], k])

            for j in range(i+1, n):
                counter[nums[j]] += 1

        return res
