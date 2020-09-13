"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def get_new_line(line_file, num):
    """
    принимает строку с английским названием цифры
    и возвращает новую строку
    с заменой английского названия на русское
    :param line_file: исходная строка текста
    :param num: цифра идентичная ключу в словаре,
    под которым лежит русский аналог названия цифры
    :return: изменённую строку с русским названием цифры
    """
    if num in rus_nums:
        rus_num = rus_nums[num]
    line_list = line.strip().split()
    line_list.remove(line_list[0])
    line_list.insert(0, rus_num)
    new_line = " ".join(line_list)
    return new_line


rus_nums = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}


if __name__ == "__main__":
    count = 1
    with open("test4.txt", "r") as t:
        for line in t:
            new_line = get_new_line(line, count)
            count += 1
            with open("new_test4.txt", 'a') as nt:
                nt.write(new_line)
                nt.write("\n")
