from src.book import Book
from src.repository import Repository

class LibraryService:
    """Сервис для управления библиотекой."""

    def __init__(self, repository: Repository):
        self.repository = repository

    def add_book(self, title: str, author: str, year: int) -> Book:
        """Добавить книгу в библиотеку."""
        book_id = max([book.id for book in self.repository.get_books()], default=0) + 1
        new_book = Book(title, author, year, book_id)
        self.repository.add_book(new_book)
        return new_book

    def remove_book(self, book_id: int) -> bool:
        """Удалить книгу из библиотеки по ID."""
        return self.repository.remove_book(book_id)

    def get_all_books(self):
        """Получить все книги."""
        return self.repository.get_books()

    def change_book_status(self, book_id: int, status: str) -> bool:
        """Изменить статус книги по ID."""
        book = self.repository.get_book_by_id(book_id)
        if book:
            book.change_status(status)
            self.repository.storage.save_books(self.repository.get_books()) 
            return True
        return False
