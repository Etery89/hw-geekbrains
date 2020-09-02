"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""
elements = []
num_elements = int(input("Пожалуйста ведите колличество элементов списка: "))
for num in range(num_elements):
    element = input("Пожалуйста введите элемент списка: ")
    elements.append(element)

print(f"Ваш список: {elements}")

num_index = 0

len_elements = len(elements)
if len_elements % 2 == 0:
    for num in range(len(elements) // 2):
        elements[num_index], elements[num_index + 1] = elements[num_index + 1], elements[num_index]
        num_index += 2
else:
    last_element = elements.pop()
    new_len_elements = len(elements)
    for num in range(len(elements) // 2):
        elements[num_index], elements[num_index + 1] = elements[num_index + 1], elements[num_index]
        num_index += 2
    elements.append(last_element)

print(f"Новый список: {elements}")
