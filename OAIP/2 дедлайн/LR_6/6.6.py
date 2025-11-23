def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("топот"))
print(is_palindrome("python"))