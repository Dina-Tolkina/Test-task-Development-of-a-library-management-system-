import unittest
from unittest.mock import MagicMock, patch
from src.cli import CLI
from src.library_service import LibraryService
from io import StringIO
import sys

class TestCLI(unittest.TestCase):

    def setUp(self):
        """Настройка для каждого теста."""

        self.mock_library_service = MagicMock(spec=LibraryService)
        self.cli = CLI(self.mock_library_service)

    def test_add_book(self):
        """Тестирование добавления книги"""

        self.mock_library_service.add_book.return_value = MagicMock(title="Test Book", author="Test Author", year=2024)

        captured_output = StringIO()
        sys.stdout = captured_output

        with patch('builtins.input', side_effect=["1", "Test Book", "Test Author", "2024", "0"]):
            self.cli.run()  

        self.mock_library_service.add_book.assert_called_with("Test Book", "Test Author", 2024)
        
        self.assertIn("Книга 'Test Book' добавлена.", captured_output.getvalue())

    def test_remove_book(self):
        """Тестирование удаления книги"""

        self.mock_library_service.remove_book.return_value = True

        captured_output = StringIO()
        sys.stdout = captured_output

        with patch('builtins.input', side_effect=["2", "1", "0"]):
            self.cli.run()  

        self.mock_library_service.remove_book.assert_called_with(1)

        self.assertIn("Книга с ID 1 удалена.", captured_output.getvalue())

    def test_view_all_books(self):
        """Тестирование просмотра всех книг"""

        self.mock_library_service.get_all_books.return_value = [
            MagicMock(id=1, title="Book 1", author="Author 1", year=2020, status="в наличии"),
            MagicMock(id=2, title="Book 2", author="Author 2", year=2021, status="выдана")
        ]

        captured_output = StringIO()
        sys.stdout = captured_output

        with patch('builtins.input', side_effect=["3", "0"]):
            self.cli.run()  

        self.mock_library_service.get_all_books.assert_called_once()
        self.assertIn("1. Book 1 - Author 1 (2020) - Статус: в наличии", captured_output.getvalue())
        self.assertIn("2. Book 2 - Author 2 (2021) - Статус: выдана", captured_output.getvalue())

    def test_change_book_status(self):
        """Тестирование изменения статуса книги"""

        self.mock_library_service.get_all_books.return_value = [
            MagicMock(id=1, title="Book 1", author="Author 1", year=2020, status="в наличии")
        ]
        self.mock_library_service.change_book_status.return_value = True

        captured_output = StringIO()
        sys.stdout = captured_output

        with patch('builtins.input', side_effect=["4", "1", "выдана", "0"]):
            self.cli.run()  

        self.mock_library_service.change_book_status.assert_called_with(1, "выдана")
        self.assertIn("Статус книги с ID 1 изменен на 'выдана'.", captured_output.getvalue())

    def test_invalid_option(self):
        """Тестирование неверного выбора"""

        captured_output = StringIO()
        sys.stdout = captured_output

        with patch('builtins.input', side_effect=["99", "0"]):
            self.cli.run() 

        self.assertIn("Неверный выбор. Попробуйте снова.", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
