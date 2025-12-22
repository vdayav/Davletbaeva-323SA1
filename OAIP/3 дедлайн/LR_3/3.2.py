def sum_digits(number):
    if number < 10:
        return number
    
    last_digit = number % 10
    remaining_part = number // 10
    return last_digit + sum_digits(remaining_part)

print(sum_digits(12345)) 