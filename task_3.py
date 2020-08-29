"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
user_num = int(input("Пожалуйста введите число от 1 до 9: "))
user_num_2 = int(str(user_num) + str(user_num))
user_num_3 = int(str(user_num_2) + str(user_num))
sum = user_num + user_num_2 + user_num_3

if __name__ == "__main__":
    print(f"Сумма чисел в формате n + nn + nnn: {sum}")