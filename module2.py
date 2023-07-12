"""Модуль 2."""
import warnings


def description_2():
    return "Функция для описания второго модуля"


def new_func():
    print("new_func_for_module_2")


warnings.warn(description_2())
