import time

from faker import Faker
from faker.providers.python import TEnum
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def email(self) -> str:
        return f"{time.time()}.{self.faker.email()}"

    def enum(self, value: type[TEnum]) -> TEnum:
        return self.faker.enum(value)

    def category(self) -> str:
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets",
        ])

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайное имя.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя.

        :return: Случайное отчество.
        """
        return self.faker.first_name()

    def phone_number(self) -> str:
        """
        Генерирует случайный номер телефона.

        :return: Случайный номер телефона.
        """
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        """
        Генерирует случайное число с плавающей запятой в указанном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное число с плавающей запятой.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Генерирует случайную денежную сумму.

        :return: Сумма от 1 до 1000.
        """
        return self.float(1, 1000)

    def proto_enum(self, value: EnumTypeWrapper) -> int:
        return self.faker.random_element(value.values())


fake = Fake(faker=Faker())
