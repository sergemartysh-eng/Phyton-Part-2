class SocialNetwork:
    """
    Базовый класс для социальных сетей.
    Атрибуты:
        name (str): название социальной сети.
        user_count (int): количество пользователей.
    Методы:
        get_description(): возвращает строку с описанием сети.
        get_category(): возвращает категорию сети.
    """

    def __init__(self, name: str, user_count: int) -> None:
        """
        Инициализация социальной сети.
        Args:
            name: название сети.
            user_count: количество пользователей.
        """
        self.name = name
        self.user_count = user_count

    def __str__(self) -> str:
        """Возвращает неформальное строковое представление."""
        return f"{self.name} (users: {self.user_count})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление."""
        return f"SocialNetwork('{self.name}', {self.user_count})"

    def get_description(self) -> str:
        """Возвращает описание социальной сети."""
        return f"This is a social network named {self.name} with {self.user_count} users."

    def get_category(self) -> str:
        """Возвращает категорию социальной сети."""
        return "General social network"


class Vk(SocialNetwork):
    """
    Класс для социальной сети VK.
    Наследует все атрибуты от SocialNetwork.
    Перегружает методы __str__, __repr__ и get_category.
    """

    def __init__(self, name: str, user_count: int) -> None:
        """Инициализация VK с помощью конструктора базового класса."""
        super().__init__(name, user_count)

    def __str__(self) -> str:
        """Возвращает неформальное строковое представление для VK."""
        return f"VK: {self.name} (users: {self.user_count})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление для VK."""
        return f"Vk('{self.name}', {self.user_count})"

    def get_category(self) -> str:
        """
        Возвращает категорию VK.
        Перегрузка метода базового класса, так как VK относится к категории
        'Социальные сети и мессенджеры' и имеет свои особенности.
        """
        return "Russian social network and messenger"


class Max(SocialNetwork):
    """
    Класс для социальной сети Max.
    Наследует все атрибуты от SocialNetwork.
    Перегружает методы __str__, __repr__ и get_category.
    """

    def __init__(self, name: str, user_count: int) -> None:
        super().__init__(name, user_count)

    def __str__(self) -> str:
        return f"Max: {self.name} (users: {self.user_count})"

    def __repr__(self) -> str:
        return f"Max('{self.name}', {self.user_count})"

    def get_category(self) -> str:
        """
        Возвращает категорию Max.
        Перегрузка, так как Max (предположительно) является частью экосистемы
        и имеет специфику.
        """
        return "Part of Mail.ru ecosystem"


class TamTam(SocialNetwork):
    """
    Класс для социальной сети TamTam.
    Наследует все атрибуты от SocialNetwork.
    Перегружает методы __str__, __repr__ и get_category.
    """

    def __init__(self, name: str, user_count: int) -> None:
        super().__init__(name, user_count)

    def __str__(self) -> str:
        return f"TamTam: {self.name} (users: {self.user_count})"

    def __repr__(self) -> str:
        return f"TamTam('{self.name}', {self.user_count})"

    def get_category(self) -> str:
        """
        Возвращает категорию TamTam.
        Перегрузка, так как TamTam ориентирован на общение и сообщества.
        """
        return "Messenger with social features"


class Odnoklassniki(SocialNetwork):
    """
    Класс для социальной сети Одноклассники.
    Наследует все атрибуты от SocialNetwork.
    Перегружает методы __str__, __repr__ и get_category.
    """

    def __init__(self, name: str, user_count: int) -> None:
        super().__init__(name, user_count)

    def __str__(self) -> str:
        return f"Odnoklassniki: {self.name} (users: {self.user_count})"

    def __repr__(self) -> str:
        return f"Odnoklassniki('{self.name}', {self.user_count})"

    def get_category(self) -> str:
        """
        Возвращает категорию Одноклассники.
        Перегрузка, так как Одноклассники ориентированы на старшее поколение
        и имеют свои особенности.
        """
        return "Social network for older generation"
