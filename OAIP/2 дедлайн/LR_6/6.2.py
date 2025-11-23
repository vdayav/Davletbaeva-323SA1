def simple_calculator(a: float, b: float, operator: str):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Неизвестный оператор"

result = simple_calculator(10, 5, '*')
print(result)