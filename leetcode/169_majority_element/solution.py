class Solution:
    def majorityElement(self, nums):
        count = 1
        candidate = nums[0]

        for num in nums[1:]:
            if num == candidate:
                count += 1
            elif count == 0:
                count = 1
                candidate = num
            else:
                count -= 1
        return candidate
