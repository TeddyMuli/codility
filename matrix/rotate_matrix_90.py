#!/usr/bin/python3
class Solution:
    def rotateMatrixBy90(self,Mat):
        rows = len(Mat)
        cols = len(Mat[0])

        new_matrix = [[i for i in range(rows)] for j in range(cols)]

        for i in range(cols):
            for j in range(rows):
                new_matrix[i][j] = Mat[rows-j-1][i]

        return new_matrix
    
if __name__ == "__main__":
    sol = Solution()
    test=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    result = sol.rotateMatrixBy90(test)
    for row in result:
        print(*row)
