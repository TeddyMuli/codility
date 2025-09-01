class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = curr_sum = 0
        min_len = float('inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                min_len = min(min_len, i - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
