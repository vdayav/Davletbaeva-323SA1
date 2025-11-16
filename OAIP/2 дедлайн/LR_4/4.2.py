numbers = [34, 67, 12, 89, 45, 78, 23, 56, 91, 30]

chetno = []  
for num in numbers:
    if num % 2 == 0:  
        chetno.append(num)  

large = [] 
for num in numbers:
    if num > 50: 
        large.append(num)  

print("Исходный список чисел:", numbers)
print("Четные числа:", chetno)
print("Числа больше 50:", large)