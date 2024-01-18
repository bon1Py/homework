class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

# Пример
book1 = Book(1, 'Война и мир', 1225)
print(book1)  # Книга "Война и мир"
print(repr(book1))  # Book(id_=1, name='Война и мир', pages=1225)

book2 = eval(repr(book1))
print(book2)  # Книга "Война и мир"
print(book2.id)  # 1
print(book2.name)  # Война и мир
print(book2.pages)  # 1225
