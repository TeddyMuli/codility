#!/usr/bin/python3
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

if __name__ == "__main__":
    sol = Solution()
    test1 = [3,2,2,3]
    test2 = [0,1,2,2,3,0,4,2]
    print(sol.removeElement(test1, 3))
    print(sol.removeElement(test2, 2))
