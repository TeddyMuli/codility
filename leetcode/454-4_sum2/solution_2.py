#!/usr/bin/python3
from collections import Counter
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        AB = Counter(a + b for a in nums1 for b in nums2)
        return sum(AB[-c-d] for c in nums3 for d in nums4)


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))
