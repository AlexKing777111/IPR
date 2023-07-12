"""
    1. Реализовать итератор и генератор возвращающие бесконечную последовательность случайных целых чисел.
    Диапазон указать в параметрах итератора и генератора.

    Объяснить в чем разница между объектами возвращаемыми генератором и итератором.

    2. Реализовать свой вариант функции next() для работы с итераторами и генераторами.
    Для реализации используем "протокол итератора".
"""
import random


class MyIterator:
    def __init__(self, range_from, range_to):
        self.range_from = range_from
        self.range_to = range_to

    def __iter__(self):
        return self

    def __next__(self):
        result = random.randint(self.range_from, self.range_to)
        return result


print("---Начало работы итератора---")
s = MyIterator(0, 2)
print(next(s))
print(next(s))
print(next(s))


def my_generator(range_from, range_to):
    while True:
        result = random.randint(range_from, range_to)
        yield result


print("---Начало работы генератора---")
r = my_generator(0, 5)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

# Разница в том, что генератор можно обойти только один раз
# Элементы генератора не хранятся в памяти, а формируются на лету
