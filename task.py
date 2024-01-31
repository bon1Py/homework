class Book:
    """ Базовый класс - Книга """

    def init(self, name: str, author: str):
        self._name = name
        self._author = author

    # name и author только для чтения, поэтому только геттер
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"Книга {self.name}. Автор {self.author}"

    def repr(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс - Бумажная книга """

    def init(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = None

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self.pages = value
        else:
            raise ValueError("Количество страниц должно быть положительным целым числом")


    # Перегрузка метода __str__ необходима для добавления информации
    # о количестве страниц в бумажной книге
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    """ Дочерний класс - Аудиокнига """

    def init(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = None

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0:
            self.duration = value
        else:
            raise ValueError("Продолжительность должна быть положительным числом с плавающей запятой")

    # Перегрузка метода __str__ необходима для добавления информации
    # о продолжительности аудиокниги
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"
