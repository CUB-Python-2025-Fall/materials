from dataclasses import dataclass
import abc


@dataclass
class Book:
    id: int
    name: str
    quantity: int


@dataclass
class User:
    id: int
    name: str
    books: list[Book]


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
    def update(self, book: Book) -> Book | None:
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
                result.append(book )
        return result

    def update(self, new_book: Book) -> Book | None:
        for book in self.books:
            if book.id == new_book.id or book.name == new_book.name:
                return None
        self.books.append(new_book)
        return new_book


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


def get_str_input(message: str) -> str:
    return input(message)


def get_int_input(message: str) -> int:
    while True:
        try:
            str_input = get_str_input(message)
            return int(str_input)
        except ValueError:
            print('Invalid input: not an integer. Please try again')


def get_int_input_in_range(message: str, range_start: int, range_end: int) -> int:
    while True:
        int_input = get_int_input(message)
        if range_start <= int_input <= range_end:
            return int_input
        else:
            print(f'Invalid input: not in range {range_start} to {range_end}')



class OperationsManager:
    def __init__(self, book_repository: BookRepositoryInterface, user_repository: UserRepositoryInterface):
        self.book_repository = book_repository
        self.user_repository = user_repository

    def print_menu(self):
        print("Program Options: ")
        options = [
            '1) Add book',
            '2) Print library books',
            '3) Print books by prefix',
            '4) Add user',
            '5) Borrow book',
            '6) Return book',
            '7) Print users borrowed book',
            '8) Print users'
        ]
        print('\n'.join(options))
        return get_int_input_in_range(f"Enter your choice from 1 to {len(options)} \n", 1, len(options))

    def add_book(self):
        book_id = get_int_input('Please Enter the book id: \n')
        book_name = get_str_input('Please Enter the book name: \n')
        book_quantity = get_int_input('Please Enter the book quantity: \n')

        old_book = self.book_repository.get_by_id(book_id)
        if old_book is not None:
            print("Book with this id already exists")
        else:
            self.book_repository.update(Book(id=book_id, name=book_name, quantity=book_quantity))
            print('Book is added successfully')

    def print_books(self):
        book_names = []
        for book in self.book_repository.get_all():
            book_names.append(book.name)
        if len(book_names) > 0:
            print(', '.join(book_names))
        else:
            print("There are no books")

    def search_books(self):
        query = get_str_input('Enter your query: \n')
        books = self.book_repository.get_by_name_query(query)
        book_strings = list(map(lambda b: str(b), books))
        print(', '.join(book_strings))

    def add_user(self):
        user_id = get_int_input('Enter user id: \n')
        user_name = get_str_input('Enter user name: \n')

        old_user = self.user_repository.get_by_id(user_id)
        if old_user is not None:
            print("User with this id already exists")
        else:
            self.user_repository.update(User(id=user_id, name=user_name, books=[]))
            print("User created successfully !")

    def borrow_book(self):
        user_id = get_int_input('Enter user id: \n')
        book_name = get_str_input('Enter book name: \n')

        user = self.user_repository.get_by_id(user_id)
        if user is None:
            print("User with this id does not exist")
            return

        book = self.book_repository.get_by_name(book_name)
        if book is None:
            print("Book with this name does not exist")
            return

        if book.quantity <= 0:
            print("Insufficient quantity!")
            return

        updated_user = self.user_repository.add_book(user_id, book)
        if updated_user is None:
            print("Failed to add book to user")
            return

        book.quantity -= 1
        self.book_repository.update(book)

        print(F'The user {updated_user.name} borrowed {book}')

    def return_book(self):
        user_id = get_int_input('Enter user id: \n')
        book_name = get_str_input('Enter book name: \n')

        user = self.user_repository.get_by_id(user_id)
        if user is None:
            print("User with this id does not exist")
            return

        book = self.book_repository.get_by_name(book_name)
        if book is None:
            print("Book with this name does not exist")
            return

        updated_user = self.user_repository.remove_book(user_id, book)
        if updated_user is None:
            print("Failed to remove book from user")
            return

        book.quantity += 1
        self.book_repository.update(book)

        print(F'The user {updated_user.name} returned {book}')

    def print_users_borrowed(self):
        users = self.user_repository.get_with_books()

        if len(users) == 0:
            print('There are no users borrowed any book')
        else:
            for user in users:
                print(f'The user {user.name} borrowed the books {" and ".join(list(map(lambda b: str(b), user.books)))}')

    def print_all_users(self):
        users = self.user_repository.get_all()

        if len(users) == 0:
            print('There are no users')
        else:
            print(" and ".join(list(map(lambda u: str(u), users))))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.search_books()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed()
            elif choice == 8:
                self.print_all_users()
            else:
                print("Exiting the program.")
                break


if __name__ == '__main__':
    main = OperationsManager(
        book_repository=ListBookRepository(),
        user_repository=DictUserRepository()
    )
    main.run()
