"""Реализовать функцию принимающую название модуля в виде строки и загружающего его."""
from importlib import import_module


def func_for_import(module_name):
    return import_module(module_name)


if __name__ == "__main__":
    module2 = func_for_import("module2")
    print("Работа функции завершена")
    module2.new_func()
