from dataclasses import dataclass
from book import Book


@dataclass
class User:
    id: int
    name: str
    books: list[Book]