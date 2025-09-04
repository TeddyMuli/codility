class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if nums is None:
            return []
        
        n = len(nums)
        result = []
        i = 0
        temp = ""
        next_num = False

        while i < n:
            temp += f"{nums[i]}"
            
            while i < n - 1 and nums[i+1] == nums[i] + 1:
                i += 1
                next_num = True

            if next_num:
                temp += f"->{nums[i]}"

            result.append(temp)
            temp = ""
            next_num = False
            i += 1

        return result
