#!/usr/bin/env python3
def solution(A):
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)

    if not peaks:
        return 0

    for i in range(len(peaks), 0, -1):
        last_flag = peaks[0]
        count = 1

        for peak in peaks[1:]:
            if peak - last_flag >= i:
                count += 1
                last_flag = peak
                if count == i:
                    break
        if count == i:
            return i

if __name__ == "__main__":
    test = [1, 5, 3]
    print(solution(test))
