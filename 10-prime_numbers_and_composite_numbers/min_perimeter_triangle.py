#!/usr/bin/env python3
def solution(N):
    for i in range(int(N**0.5), 1, -1):
        if N % i == 0:
            sideA = i
            break

    sideB = N / sideA
    perimeter = 2*(sideA+sideB)

    return int(perimeter)

if __name__ == "__main__":
    test = 30
    print(solution(test))
