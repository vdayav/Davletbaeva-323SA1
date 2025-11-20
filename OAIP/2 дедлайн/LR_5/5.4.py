text = input("Введите текст: ")

words = text.lower().split()
unique = set(words)
print(f"Уникальные слова: {len(unique)}")

long = {word for word in unique if len(word) > 5}
print(f"Длинные слова: {long}")

key_words = {'python', 'programming'}
found_keywords = key_words & unique 

print(f"Найдены ключевые слова: {bool(found_keywords)}")