"""
7. Реализовать проект «Операции с комплексными числами».
 Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    imaginary_unit = 1j

    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def get_complex_num(self):
        return self.real_part + self.imaginary_part * self.imaginary_unit

    def __add__(self, other):
        return self.real_part + other.real_part + self.imaginary_unit * (self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        augend = (self.real_part * other.real_part - self.imaginary_part * other.imaginary_part) * self.imaginary_unit
        second_summand = (self.imaginary_part * other.real_part + self.real_part * other.imaginary_part) * self.imaginary_unit
        return augend + second_summand


complex_num_1 = ComplexNumber(1, 3)
print(complex_num_1.get_complex_num())
complex_num_2 = ComplexNumber(3, 2)
print(complex_num_2.get_complex_num())
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)




