

# TODO Написать 3 класса с документацией и аннотацией типов

class Book:


    def __init__(self, title: str, author: str, pages: int):

        if not title:
            raise ValueError("Название книги не отсутствовать")
        if not author:
            raise ValueError("Автор книги не может отсутствовать")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self) -> str:

        return f'Книга "{self.title}" автора {self.author}, {self.pages} страниц'

    def read_page(self, page_number: int) -> str:

        if page_number < 1 or page_number > self.pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.pages}")
        return f'Читаем страницу {page_number} из книги "{self.title}"'

    def calculate_reading_time(self, pages_per_hour: int) -> float:

        return self.pages / pages_per_hour


class Car:

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0.0):
        import datetime

        if not brand:
            raise ValueError("Марка автомобиля не может отсутствовать")
        if not model:
            raise ValueError("Модель автомобиля не может отсутствовать")
        if year < 1886 or year > datetime.datetime.now().year:
            raise ValueError(f"Год выпуска должен быть между 1886 и {datetime.datetime.now().year}")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным")

        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance: float) -> None:

        if current_year < self.year:
            raise ValueError("Текущий год не может быть меньше года выпуска")
        return current_year - self.year

    def get_info(self) -> str:

        return f'{self.brand} {self.model} {self.year} года выпуска, пробег: {self.mileage} км'


class BankAccount:

    def __init__(self, account_number: str, owner: str, balance: float = 0.0, currency: str = "RUB"):

        if not account_number:
            raise ValueError("Номер счета не может отсутствовать")
        if not owner:
            raise ValueError("Владелец счета не может отсутствовать")
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self) -> str:
        return f'Баланс счета: {self.balance} {self.currency}'


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod(verbose=True)
