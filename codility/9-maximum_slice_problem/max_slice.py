#!/usr/bin/env python3
def solution(A):
    # This uses Kadane's algorithm
    if not A:
        return 0

    current_sum = max_sum = A[0]
    # we start with A[0] instead of 0 for the following reasons:
    # 1. we need to consider -ve values
    # 2. we need atleast one number
    
    for num in A[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    test = [-5, -1]
    print(solution(test))
