"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("test2.txt", 'r') as t:
    text = t.read()
    count_lines = text.strip().split("\n")
    count_words = text.strip().split()
    print(f"Количество строк в файле: {len(count_lines)}")
    print(f"Количество слов в файле: {len(count_words)}")

