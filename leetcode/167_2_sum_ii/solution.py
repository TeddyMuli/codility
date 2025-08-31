class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            su_m = numbers[left] + numbers[right]
            if su_m == target:
                return [left+1, right+1]
            elif su_m < target:
                left+=1
            else:
                right-=1
