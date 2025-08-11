#!/usr/bin/python3
class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        number = 1
        left = top = 0
        right = bottom = n - 1

        while number <= n**2:
            for i in range(left, right + 1):
                matrix[top][i] = number
                number += 1
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][right] = number
                number += 1
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = number
                number += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = number
                number += 1
            left += 1

        return matrix

if __name__ == "__main__":
    sol = Solution()
    test = 3
    print(sol.generateMatrix(test))
