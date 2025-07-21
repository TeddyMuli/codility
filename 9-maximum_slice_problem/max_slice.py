#!/usr/bin/env python3
def solution(A):
    # This uses Kadane's algorithm
    if not A:
        return 0

    current_sum = max_sum = A[0]
    
    for num in A[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    test = [3,2,-6,4,0]
    print(solution(test))
