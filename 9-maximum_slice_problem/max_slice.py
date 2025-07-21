#!/usr/bin/env python3
def solution(A):
    # This uses Kadane's algorithm
    current_sum = max_sum = 0
    
    for num in A:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    test = [3,2,-6,4,0]
    print(solution(test))
