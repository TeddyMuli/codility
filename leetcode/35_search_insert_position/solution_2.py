class Solution:
    def searchInsert(self, nums, target):
        # use binary search
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 7
    sol = Solution()
    print(sol.searchInsert(nums, target))
