#!/usr/bin/python3
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        n = len(nums1)
        tuples = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            tuples.append((i, j, k, l))

        return len(tuples)

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))
