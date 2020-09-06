"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def generation_user_info(name, surname, year_of_birth, city_of_residence, email, phone_number):
    user_info = {"name": name, "surname": surname, "year_of_birth": year_of_birth,
                 "city_of_residence": city_of_residence, "email": email, "phone_number": phone_number}
    return user_info


if __name__ == "__main__":
    user_name, user_surname = input("Пожалуйста введите свои имя и фамилию: ").split()
    user_birth = int(input("Пожалуйста введите год своего рождения: "))
    user_city = input("Пожалуйста введите город вашего проживания: ")
    user_email = input("Введите адрес электронной почты: ")
    user_phone = int(input("Номер телефона в формате '9XXXXXXXXX': "))
    user_information = generation_user_info(name=user_name,
                                            surname=user_surname,
                                            year_of_birth=user_birth,
                                            city_of_residence=user_city,
                                            email=user_email,
                                            phone_number=user_phone
                                            )
print(f"Ваши данные: {user_information['name']} {user_information['surname']}, {user_information['year_of_birth']} г.р., {user_information['city_of_residence']}, email: {user_information['email']}, тел. {user_information['phone_number']}")
print("Ваши данные: ",
      user_information['name'],
      user_information['surname'],
      user_information['year_of_birth'],
      user_information['city_of_residence'],
      user_information['email'],
      user_information['phone_number'],
      sep='\n')
