import abc
from book import Book


class BookRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> Book | None:
        pass

    @abc.abstractmethod
    def get_by_name(self, name: str) -> Book | None:
        pass

    @abc.abstractmethod
    def get_by_name_query(self, query: str) -> list[Book]:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[Book]:
        pass

    @abc.abstractmethod
    def create(self, book: Book) -> Book | None:
        pass


class ListBookRepository(BookRepositoryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def get_by_id(self, id: int) -> Book | None:
        for book in self.books:
            if book.id == id:
                return book
        return None

    def get_all(self) -> list[Book]:
        result = []
        for book in self.books:
            result.append(book)
        return result

    def get_by_name(self, name: str) -> Book | None:
        for book in self.books:
            if book.name == name:
                return book
        return None

    def get_by_name_query(self, query: str) -> list[Book]:
        result = []
        for book in self.books:
            if book.name[:len(query)].upper() == query.upper():
                result.append(book)
        return result

    def create(self, new_book: Book) -> Book | None:
        for book in self.books:
            if book.id == new_book.id or book.name == new_book.name:
                return None
        self.books.append(new_book)
        return new_book
