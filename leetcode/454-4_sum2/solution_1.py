#!/usr/bin/python3
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = 0
        n = len(nums1)
        nums_map = defaultdict(int)

        for i in range(n):
            for j in range(n):
                s = nums1[i] + nums2[j]
                nums_map[s] += 1
        
        for i in range(n):
            for j in range(n):
                target = -(nums3[i] + nums4[j])
                if target in nums_map:
                    count += nums_map[target]

        return count

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))
