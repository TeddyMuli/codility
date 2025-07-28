#!/usr/bin/env python3
def solution(A):
    min_price = float("inf")
    max_profit = 0

    for price in A:
        if price < min_price:
            min_price = price
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

if __name__ == "__main__":
    test = [23171, 21011, 21123, 21366, 21013, 21367]
    print(solution(test))
