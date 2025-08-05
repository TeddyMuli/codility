#!/usr/bin/python3
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        numsMap = {}

        for i in range(n):
            numsMap[nums[i]] = i

        for i in range(n):
            compliment = target - nums[i]
            if compliment in numsMap and numsMap[compliment] != i:
                return [i, numsMap[compliment]]
            
        return []

if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,11,15]
    print(sol.twoSum(nums, 9))
    nums = [3,2,4]
    print(sol.twoSum(nums, 6))    
