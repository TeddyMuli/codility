#!/usr/bin/python3
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) < 1:
            return 0
        nums = sorted(set(nums))
        max_count = 0
        current_count = 1
        first = nums[0]

        for num in nums[1:]:
            if num == first + 1:
                current_count += 1
            else:
                max_count = max(current_count, max_count)
                current_count = 1
            first = num

        max_count = max(current_count, max_count)

        return max_count

if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,1,2]
    print(sol.longestConsecutive(nums))
