#!/usr/bin/python3
def rotate90(matrix):
    n = len(matrix)
    new = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-1-i] = matrix[i][j]
    return new

if __name__ == "__main__":
    test=[[1,2,3], [4,5,6],[7,8,9]]
    print(rotate90(test))

