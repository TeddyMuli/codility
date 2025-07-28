#!/usr/bin/python3
class Solution:
    def sortedMatrix(self,N,Mat):
        elements = [Mat[i][j] for i in range(N) for j in range(N)]
        elements.sort()

        k=0
        for i in range(N):
            for j in range(N):
                Mat[i][j] = elements[k]
                k+=1
    
        for i in range(N):
            for j in range(N):
                print(Mat[i][j], end=" ")
            print('\n')

if __name__ == "__main__":
    solution = Solution()
    test=[[10,20,30,40],
        [15,25,35,45],
        [27,29,37,48],
        [32,33,39,50]]
    solution.sortedMatrix(4, test)
