import doctest


class Character:
    """
    Документация на класс.
    Класс описывает модель персонажа компьютерной игры
    """
    def __init__(self, HP: int, damage: int, weapon: str):
        """
        Инициализация экземпляра класса "Персонаж".

        :param HP: Базовый показатель здоровья
        :param damage: Базовый показатель урона
        :param weapon: Тип используемого оружия

        Пример:
        >>> theHunter = Character(3000, 150, "bow")
        """
        self.HP = 3000      # базовый показатель здоровья
        if not isinstance(HP, int):
            self.HP = round(HP)
        if HP <= 0:
            raise ValueError("Показатель здоровья - положительное число")

        self.damage = 100   # базовый показатель урона
        if not isinstance(damage, int):
            self.damage = round(damage)
        if damage <= 0:
            raise ValueError("Показатель урона - положительное число")

        self.weapon = "bow"     # тип оружия
        if not isinstance(weapon, str):
            raise TypeError("Требуемый тип данных - str")

    def HP_LVL_growth(self, LVL: int) -> int:
        """
        Метод задает закон увеличения показателя здоровья с повышением уровня персонажа
        и позволяет определить показатель здоровья для заданного уровня.

        :param LVL: Уровень персонажа
        :return: Базовый показатель здоровья персонажа на уровне LVL

        Пример
        >>> theHunter = Character(3000, 150, "bow")
        >>> theHunter.HP_LVL_growth(10)
        """

        # какая-то составная супер-формула, которая учитывает все тонкости геймплея

        ...

    def damage_LVL_growth(self, LVL: int) -> int:
        """
        Метод задает закон увеличения показателя урона с повышением уровня персонажа
        и позволяет определить показатель урона для заданного уровня и типа оружия.

        :param LVL: Уровень персонажа
        :return: Базовый показатель урона персонажа с типом оружия weapon на уровне LVL

        Пример
        >>> theHunter = Character(3000, 150, "bow")
        >>> theHunter.damage_LVL_growth(10)
        """

        # какая-то составная супер-формула, которая учитывает все тонкости геймплея
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class AcademicSubject:
    """
    Документация на класс.
    Класс описывает учебную дисциплину в ЭИОС.
    """
    def __init__(self, name: str, count_training: int, count_checkout: int, final_test_type: str):
        """
        Инициализация экземпляра класса "Учебная дисциплина".

        :param name: Наименование дисциплины
        :param count_training: Количество часов в неделю
        :param count_checkout: Количество зачетных единиц
        :param final_test_type: Вид итогового контроля

        Пример:
        >>> math = AcademicSubject("Математика", 168, 4,  "exam")
        """
        self.name = "Математика"
        if isinstance(name, str):
            raise TypeError("")

        self.count_trainig = 168
        if isinstance(count_training, int):
            raise TypeError("")
        if count_training <= 0:
            raise ValueError("")

        self.count_checkout = 3
        if isinstance(count_checkout, int):
            raise TypeError("")
        if count_checkout <= 0:
            raise ValueError("")

        self.final_test_type = "exam"
        if isinstance(final_test_type, str):
            raise TypeError("")
        ...

    def print_test(self, data: str, version: int):
        """
        Метод готовит билеты для тестирования обучающихся.

        :param data: Вопросы для тестирования. Рекомендуется прочитывать из файла
        :param version: Требуемое количество вариантов
        :return: Файл .txt

        Пример:
        >>> math = AcademicSubject("Математика", 168, 4,  "exam")
        >>> # with open(input.txt, 'r') as data
        >>> math.print_test(data, 10)
        """
        # код, который подготовит новый файл с вариантами теста и нивелирует все кривости в файле data
        ...

    def print_table(self, students: str):
        """
        Метод составляет таблицу-ведомость успеваемости для заданного списка студентов

        :param students: Список студентов
        :return: Файл .txt

        Пример:
        >>> math = AcademicSubject("Математика", 168, 4,  "exam")
        >>> # with open(input.txt, 'r') as students
        >>> math.print_test(students)
        """
        # код, который создат файл с таблицей, которую удобно использовать в работе
        ...


class FlatFigure:
    """
    Документация на класс.
    Класс описывает выпуклую плоскую фигуру.
    """
    def __init__(self, xlist: list[float | int], ylist: list[float | int]):
        """
        Инициализация экземпляра класса "Плоская фигура".

        :param xlist: Массив координат Х вершин фигуры
        :param ylist: Массив координат Y вершин фигуры

        Пример:
        >>> figure = FlatFigure([0, -1.5, -0.2, 2], [0, 2.1, 3.14, 1.3])
        """
        self.xlist = [0, 0, 1, 1]
        self.ylist = [0, 1, 1, 0]

        for x in xlist:
            if isinstance(x, float | int):
                raise TypeError("TypeError в векторе координат Х")

        for y in ylist:
            if isinstance(y, float | int):
                raise TypeError("TypeError в векторе координат Y")

        if len(xlist) != len(ylist):
            raise ValueError("Длины координатных векторов не совпадают")

        if ...:
            ...     # Проверка на выпуклость фигуры

        ...

    def area(self) -> float:
        """
        Метод вычисляет площадь выпуклой фигуры по формуле Герона

        :return: Площадь фигуры

        Пример:
        >>> figure = FlatFigure([0, -1.5, -0.2, 2], [0, 2.1, 3.14, 1.3])
        >>> figure.area()
        """

        ...

    def center_of_gravity(self) -> list[float]:
        """
        Метод вычисляет центр тяжести выпуклой фигуры

        :return: Центр масс фигуры

        Пример:
        >>> figure = FlatFigure([0, -1.5, -0.2, 2], [0, 2.1, 3.14, 1.3])
        >>> figure.center_of_gravity()
        """

        ...
