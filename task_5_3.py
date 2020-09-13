"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("test3.txt", "r") as t:
    text = t.read()
    lines = text.strip().split("\n")
    count_lines = len(text.strip().split("\n"))
    for line in lines:
        line_list = line.split()
        for elem in line_list:
            if elem.isdigit() and int(elem) < 20000:
                print(f"Cотрудник {line_list[0]} получает зарплату меньше МРОТ")
