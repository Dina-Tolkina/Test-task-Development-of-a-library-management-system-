from typing import List
from src.book import Book
from src.file_storage import FileStorage

class Repository:
    """Репозиторий для работы с книгами."""

    def __init__(self, storage: FileStorage):
        self.storage = storage
        self.books = self.storage.load_books() 

    def add_book(self, book: Book) -> None:
        """Добавить книгу в репозиторий."""
        self.books.append(book)
        self.storage.save_books(self.books)

    def remove_book(self, book_id: int) -> bool:
        """Удалить книгу из репозитория по ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.storage.save_books(self.books)
                return True
        return False

    def get_books(self) -> List[Book]:
        """Получить все книги."""
        return self.books

    def get_book_by_id(self, book_id: int) -> Book:
        """Получить книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None
