"""
1. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""
name_user = 'Alex'
the_age_of_access = 18

if __name__ == '__main__':
    surname_user = input('Пожалуйста введите свою фамилию: ')
    age_user = int(input('Пожалуйста введите свой возраст: '))
    print(name_user)
    print(surname_user)
    if age_user > the_age_of_access:
        print('Доступ разрешён')
    else:
        print('Доступ запрещён')