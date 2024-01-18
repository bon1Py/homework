class Library:
    def __init__(self, books):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1]['id'] + 1

    def get_index_by_book_id(self, book_id):
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")