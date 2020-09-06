"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
letters_low = ['a', 'b', 'c', 'd', 'e',
               'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y',
               'z']
letters_up = ['A', 'B', 'C', 'D', 'E',
              'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y',
              'Z']


def int_func1(word):
    if word[0].istitle():
        return word
    else:
        return word.title()


def int_func2(word):
    word_list = list(word)
    if word_list[0] in letters_low:
        ind = letters_low.index(word_list[0])
        word_list.pop(0)
        word_list.insert(0, letters_up[ind])
        new_word = "".join(word_list)
        return new_word
    else:
        return word


if __name__ == "__main__":
    user_str = input("Пожалуйста введите любую строку: ").split()
    new_user_str1 = []
    new_user_str2 = []
    for word in user_str:
        word1 = int_func1(word)
        new_user_str1.append(word1)
        word2 = int_func2(word)
        new_user_str2.append(word2)
    print(" ".join(new_user_str1))
    print(" ".join(new_user_str2))



