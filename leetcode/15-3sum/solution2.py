"""
This solution uses the 2 pointer approach
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if sum_3 > 0:
                    right -= 1
                elif sum_3 < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left -1]:
                        left += 1

        return res
