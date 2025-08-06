#!/usr/bin/python3
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = 0
        nums_map = defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                nums_map[num1+num2] += 1
        
        for num3 in nums3:
            for num4 in nums4:
                count += nums_map[-num3-num4]

        return count

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))
