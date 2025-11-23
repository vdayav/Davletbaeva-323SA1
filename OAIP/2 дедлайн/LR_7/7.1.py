def sum_numbers(*numbers: float):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4, 5))