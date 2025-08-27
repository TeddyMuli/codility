#!/usr/bin/python3
class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]

        return k

if __name__ == "__main__":
    sol = Solution()
    test1 = [1,1,2]
    test2 = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(test1))
    print(sol.removeDuplicates(test2))
