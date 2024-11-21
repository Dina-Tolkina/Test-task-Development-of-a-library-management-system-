import json
from typing import List
from src.book import Book

class FileStorage:
    """Инфраструктура для чтения и записи в файл."""

    def __init__(self, filename: str):
        self.filename = filename

    def load_books(self) -> List[Book]:
        """Загружает книги из файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                book_data = json.load(file)
                return [Book.from_dict(book) for book in book_data]  
        except (FileNotFoundError, json.JSONDecodeError):
            return []  

    def save_books(self, books: List[Book]) -> None:
        """Сохраняет книги в файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([book.__dict__ for book in books], file, ensure_ascii=False, indent=4)
