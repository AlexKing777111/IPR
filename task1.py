"""
    Преобразовать положительное число в кортеж цифр в обатном порядке:
    1234 => (4, 3, 2, 1)
    1+. Говорят, есть решение в одну строку.
"""
number = 1234
a = []
for i in str(number):
    a.append(int(i))
a.reverse()
b = tuple(a)
print(b)
