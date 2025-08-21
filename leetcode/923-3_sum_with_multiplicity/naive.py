#!/usr/bin/python3
class Solution(object):
    def threeSumMulti(self, arr, target):
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if arr[i]+arr[j]+arr[k] == target:
                        count += 1
                    
        return count

if __name__ == "__main__":
    sol = Solution()
    test = [1,1,2,2,3,3,4,4,5,5]
    print(sol.threeSumMulti(test, 8))
