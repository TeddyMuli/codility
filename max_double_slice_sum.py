#!/usr/bin/env python3
"""
Find the maxium double slice sum
"""
def solution(A):
    # create 2 arrays, max start that stores values from end
    # and max end that stores from start
    # loop through the different arrays with different values of Y to find the max sum
    n = len(A)
    max_start = [0] * n
    max_end = [0] * n

    for i in range(1, n-1):
        max_end[i] = max(0, A[i], A[i] + max_end[i-1])
    
    for i in range(n-2, 0, -1):
        max_start[i] = max(0, A[i], A[i] + max_start[i+1])

    result = 0
    for Y in range(1, n-1):
        result = max(result, max_end[Y-1] + max_start[Y+1])

    return result

if __name__ == "__main__":
    test1 = [3, 2, 6, -1, 4, 5, -1, 2]
    print(solution(test1))
