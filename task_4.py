"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
user_num = input("Пожалуйста введите целое положительное число: ")
len_user_num = len(user_num)
count = 0
max = int(user_num[0])

while count < len_user_num:
    num = int(user_num[count])
    if num > max:
        max = num
    count += 1

if __name__ == "__main__":
    print(f"Самая большая цифра во введённом вами числе: {max}")