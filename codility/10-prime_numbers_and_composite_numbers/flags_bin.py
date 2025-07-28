#!/usr/bin/env python3
def solution(A):
    n = len(A)
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)

    if not peaks:
        return 0
    
    def can_place_flags(k):
        last_flag = peaks[0]
        count = 1

        for peak in peaks[1:]:
            if peak - last_flag >= k:
                count += 1
                last_flag = peak
                if count == k:
                    return True
        return False

    left = 1
    right = min(len(peaks), int(n ** .5) + 1)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_flags(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


if __name__ == "__main__":
    test = [1, 5, 3]
    print(solution(test))
