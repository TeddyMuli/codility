#!/usr/bin/python3
def solution(A):
    n = len(A)
    b = [0] * n

    for i in range(n):
        b[i] = a[i]
        if i > 0:
            b[i] += a[i-1]
        if i < n-1:
            b[i] += a[i+1]

    return b

if __name__ == "__main__":
    a = [4, 0, 1, -2, 3]
    print(f"Solution: {solution(a)}")
