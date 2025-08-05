#!/usr/bin/python3
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) < 1:
            return 0
        
        best = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                next = num + 1
                while next in nums:
                    next += 1
                best = max(best, next - num)

        return best

if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,1,2]
    print(sol.longestConsecutive(nums))
