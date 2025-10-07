import abc
from user import User
from book import Book


class UserRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def get_by_id(self, id: int) -> User | None:
        pass

    @abc.abstractmethod
    def update(self, user: User) -> User | None:
        pass

    @abc.abstractmethod
    def add_book(self, user_id: int, book: Book) -> User | None:
        pass

    @abc.abstractmethod
    def remove_book(self, user_id: int, book: Book) -> User | None:
        pass

    @abc.abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abc.abstractmethod
    def get_with_books(self) -> list[User]:
        pass


class DictUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users: dict[int, User] = {}

    def get_by_id(self, id: int) -> User | None:
        return self.users.get(id, None)

    def update(self, user: User) -> User | None:
        self.users[user.id] = user
        return user

    def add_book(self, user_id: int, book: Book) -> User | None:
        user = self.users.get(user_id, None)
        if user is None:
            return None
        for other_book in user.books:
            if other_book.id == book.id:
                return None
        user.books.append(book)
        return user

    def remove_book(self, user_id: int, book: Book) -> User | None:
        user = self.users.get(user_id, None)
        if user is None:
            return None
        for i, other_book in enumerate(user.books):
            if other_book.id == book.id:
                user.books.pop(i)
                return user
        return None

    def get_all(self) -> list[User]:
        return list(self.users.values())

    def get_with_books(self) -> list[User]:
        result = []
        for user in self.users.values():
            if len(user.books) > 0:
                result.append(user)
        return result
