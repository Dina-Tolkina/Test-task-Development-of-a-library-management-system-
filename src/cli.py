from src.library_service import LibraryService

class CLI:
    """Консольный интерфейс для взаимодействия с пользователем."""

    def __init__(self, library_service: LibraryService):
        self.library_service = library_service

    def display_menu(self):
        """Отображение меню команд."""
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Показать все книги")
        print("4. Изменить статус книги")
        print("0. Выход")

    def run(self):
        """Основной цикл интерфейса."""
        while True:
            self.display_menu()
            choice = input("Выберите действие: ")

            if choice == "1":
                title = input("Название книги: ")
                author = input("Автор книги: ")
                while True:
                    try:
                        year = int(input("Год издания: "))
                        break  
                    except ValueError:
                        print("Ошибка! Введите год издания в формате числа.")
                book = self.library_service.add_book(title, author, year)
                print(f"Книга '{book.title}' добавлена.")
            elif choice == "2":
                book_id = int(input("Введите ID книги для удаления: "))
                if self.library_service.remove_book(book_id):
                    print(f"Книга с ID {book_id} удалена.")
                else:
                    print(f"Книга с ID {book_id} не найдена.")
            elif choice == "3":
                print("Список книг: ")
                books = self.library_service.get_all_books()
                if not books:
                    print("Книги отсутствуют.")
                else:
                    for book in books:
                        print(f"{book.id}. {book.title} - {book.author} ({book.year}) - Статус: {book.status}")
                print()
            elif choice == "4":
                book_id = input("Введите ID книги для изменения статуса: ")

                try:
                    book_id = int(book_id)
                except ValueError:
                    print("Ошибка! ID должен быть числом.")
                    continue  

                books = self.library_service.get_all_books()
                if not any(book.id == book_id for book in books):
                    print(f"Книга с ID {book_id} не найдена.")
                    continue  

                status = input("Введите новый статус ('в наличии' или 'выдана'): ").lower()

                if status not in ['в наличии', 'выдана']:
                    print("Ошибка! Статус должен быть 'в наличии' или 'выдана'.")
                    continue 

                if self.library_service.change_book_status(book_id, status):
                    print(f"Статус книги с ID {book_id} изменен на '{status}'.")
                else:
                    print(f"Не удалось изменить статус книги с ID {book_id}.")
            elif choice == "0":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

