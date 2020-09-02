"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""
user_string = input("Пожалуйста введите строчку из любимой песни: ")

words = user_string.split()
num_string = 1

for word in words:
    if len(word) < 10:
        print(f"{num_string}. {word}")
    else:
        print(f"{num_string}. {word[:11]}")
    num_string += 1
