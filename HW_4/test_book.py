import unittest
from unittest.mock import Mock

from book import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.book_service = BookService(Mock())

    def test_find_by_id(self):
        self.book_service.find_by_id(7)
        self.book_service.book_repo.find_by_id.assert_called_with(7)

    def test_find_all(self):
        self.book_service.find_all()
        self.book_service.book_repo.find_all.assert_called_once()


