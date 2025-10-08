from book_repository import ListBookRepository
from user_repository import DictUserRepository
from operations_manager import OperationsManager


if __name__ == '__main__':
    main = OperationsManager(
        book_repository=ListBookRepository(),
        user_repository=DictUserRepository()
    )
    main.run()
