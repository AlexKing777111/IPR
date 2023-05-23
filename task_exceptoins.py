"""
    Реализовать исключение, так чтобы оно при отправке в print() выводило:
    - название исключения;
    - описание события. Указывается в момент создания;
    - время возникновения исключения.
"""
import time


class CustomException(Exception):
    def __init__(self, description, *args: object) -> None:
        self.description = description
        super().__init__(*args)

    def __str__(self):
        return f"Это класс CustomException. Описание события: {self.description}. Исключение возникло в {time.strftime('%X')}"


print(CustomException("Какое-то описание"))
