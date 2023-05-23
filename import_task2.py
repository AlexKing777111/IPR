from importlib import import_module


def func_for_import(module_name):
    import_module(module_name)


if __name__ == "__main__":
    func_for_import("module2")
    print("Работа функции завершена")
