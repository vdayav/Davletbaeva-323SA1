a = int(input("Введите число: "))
b = int(input("Введите число: "))
result = a * b
print (f"Результат произведения: {result}")

input_values = input("Введите три целых числа через пробел: ").split( )
a, b, c = map(int, input_values)
mult_ab = a * b
mult_bc = b * c
mult_ca = c * a
print("\nРезультаты умножения:")
print(f"a * b = {a} * {b} = {mult_ab}")
print(f"b * c = {b} * {c} = {mult_bc}")
print(f"c * a = {c} * {a} = {mult_ca}")

fio = input("Введите ФИО: ").split()
print(fio[0])
print(fio[1])
print(fio[2])

numbers = input("Введите 5 чисел через пробел: ").split()
min_num = min(numbers)
max_num = max(numbers)
print("Минимальное число:", min_num)
print("Максимальное число:", max_num)

import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

message = input("Введите сообщение: ")

n = int(input("Введите количество подстановочных символов: "))

encoded_message = ""
for char in message:
    encoded_message += char + generate_random_string(n)

print("Закодированное сообщение:", encoded_message)

