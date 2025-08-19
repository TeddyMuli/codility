#!/usr/bin/python3
def solution(numbers):
    max_power = max(numbers) * 2
    powers = set()
    p = 1

    while p <= max_power:
        powers.add(p)
        p *= 2

    numbers_set = set(numbers)
    count = 0
    value_to_index = {val:num for num, val in enumerate(numbers)}

    for i in range(len(numbers)):
        for p in powers:
            target = p - numbers[i]
            if target in numbers_set:
                j = value_to_index[target]
                if i <= j:
                    count += 1

    return count

if __name__ == "__main__":
    numbers = [1, -1, 2, 3]
    print(solution(numbers))
