from copy import deepcopy
from typing import List


class Book:
    def __init__(self, id: int, title: str, author: str):
        self._id = id
        self._title = title
        self._author = author

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author


class BookRepository:
    def __init__(self, book_list: List[Book] = None):
        self._book_list = book_list
        if book_list is None:
            self._book_list = []

    def find_by_id(self, book_id: int) -> Book:
        for book in self._book_list:
            if book.id == book_id:
                return book

    def find_all(self) -> List[Book]:
        return deepcopy(self._book_list)


class BookService:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    @property
    def book_repo(self):
        return self._book_repo

    def find_by_id(self, book_id: int) -> Book:
        return self._book_repo.find_by_id(book_id)

    def find_all(self) -> List[Book]:
        return self._book_repo.find_all()
