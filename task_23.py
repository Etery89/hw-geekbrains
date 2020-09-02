"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
months_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
months_dict = {
    "зима": [12, 1, 2],
    "весна": [3, 4, 5],
    "лето": [6, 7, 8],
    "осень": [9, 10, 11]
}

num_month = int(input("Пожалуйста введите номер месяца: "))

# решение с использованием списка:
if num_month in months_list[:3]:
    print(f"Месяц под номером {num_month} - это зимний месяц")
elif num_month in months_list[3:6]:
    print(f"Месяц под номером {num_month} - это весенний месяц")
elif num_month in months_list[6:9]:
    print(f"Месяц под номером {num_month} - это летний месяц")
elif num_month in months_list[9:]:
    print(f"Месяц под номером {num_month} - это осенний месяц")

# решение с использованием словаря:
if num_month in months_dict["зима"]:
    print(f"Месяц под номером {num_month} - это зимний месяц")
elif num_month in months_dict["весна"]:
    print(f"Месяц под номером {num_month} - это весенний месяц")
elif num_month in months_dict["лето"]:
    print(f"Месяц под номером {num_month} - это летний месяц")
elif num_month in months_dict["осень"]:
    print(f"Месяц под номером {num_month} - это осенний месяц")
