def solution(A):
    min_price = float("inf")
    max_profit = 0

    for price in A:
        if price < min_price:
            min_price = price
        max_profit = price - min_price

    return max_profit

if __name__ == "__main__":
    test = []
    print(solution(test))
