a = int(input("Введите число: "))
b = int(input("Введите число: "))
result = a * b
print (f"Результат произведения: {result}")

input_values = input("Введите три целых числа через пробел: ").split()
a, b, c = map(int, input_values)
mult_ab = a * b
mult_bc = b * c
mult_ca = c * a
print("\nРезультаты умножения:")
print(f"a * b = {a} * {b} = {mult_ab}")
print(f"b * c = {b} * {c} = {mult_bc}")
print(f"c * a = {c} * {a} = {mult_ca}")

