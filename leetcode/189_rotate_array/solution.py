class Solution:
    def rotateArray(self, nums, k):
        # rotate the whole array
        # rotate the first k part of the array
        # rotate the last k part of the array
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
