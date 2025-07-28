class Solution:
    def rotateMatrix(self, M, N, Mat):
        top = 0
        bottom = M - 1
        right = N-1
        left = 0

        while top < bottom and left < right:
            prev = Mat[top+1][left]

            for i in range(left, right+1):
                Mat[top][i], prev = prev, Mat[top][i]
            top+=1

            for i in range(top, bottom+1):
                Mat[i][right], prev = prev, Mat[i][right]
            right -= 1
            
            for i in range(right, left-1, -1):
                Mat[bottom][i], prev = prev, Mat[bottom][i]
            bottom-=1

            for i in range(bottom, top-1, -1):
                Mat[i][left], prev = prev, Mat[i][left]
            left+= 1

        return Mat

if __name__ == "__main__":
    test = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    m = len(test)
    n = len(test[0])
    solution = Solution()
    print(solution.rotateMatrix(m, n, test))
