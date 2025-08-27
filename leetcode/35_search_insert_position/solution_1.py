class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
        return i + 1

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    sol = Solution()
    print(sol.searchInsert(nums, target))
