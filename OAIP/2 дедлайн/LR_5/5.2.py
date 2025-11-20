students = [ ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Мария", 19, 4.8),
    ("Иван", 20, 4.1),
    ("Ольга", 23, 4.6) ]
print("Исходный список студентов:")
for student in students:
    print(f"- {student[0]} ({student[1]} лет), средний балл: {student[2]}")

print("Студенты старше 20 лет:")
found_older = False
for name, age, avg_score in students:  
    if age > 20:
        print(f"- {name} ({age}), средний балл: {avg_score}")
        found_older = True

if not found_older:
    print("Студентов старше 20 лет не найдено")

best_student = students[0]  
for student in students:
    if student[2] > best_student[2]: 
        best_student = student

print(f"Лучший студент: {best_student[0]}, средний балл: {best_student[2]}")

sort = sorted(students, key=lambda student: student[0])

print("Студенты, отсортированные по имени:")
for name, age, avg_score in sort:
    print(f"- {name} ({age} лет), средний балл: {avg_score}")