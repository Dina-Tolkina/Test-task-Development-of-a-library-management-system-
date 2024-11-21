# Тестовое задание (Разработка системы управления библиотекой)
## Описание  
Проект представляет собой систему управления библиотекой, разработанную на языке Python. 
Система позволяет пользователям взаимодействовать с библиотечным каталогом через консольный интерфейс, добавлять, 
удалять, просматривать книги и изменять их статус.

## Содержание
- [Основные функции](#основные-функции)
- [Технологии](#технологии)
- [Как установить и запустить](#как-установить-и-запустить)
- [Тестирование](#тестирование)

## Основные функции:
1. Добавление книги
Позволяет добавить новую книгу в библиотеку. Для добавления требуется указать название, автора и год издания. Возвращает информацию о добавленной книге.
2. Удаление книги
Удаляет книгу из библиотеки по её уникальному идентификатору (ID). Если удаление выполнено успешно, возвращает True. Если книга с указанным ID не найдена, возвращает False.
3. Просмотр всех книг
Предоставляет полный список книг, доступных в библиотеке. Для каждой книги отображаются её ID, название, автор, год издания и текущий статус (например, "в наличии" или "выдана").
4. Изменение статуса книги
Позволяет обновить статус книги по её ID. Возможные статусы: "в наличии" или "выдана". Если обновление выполнено успешно, возвращает True. Если книга с указанным ID не найдена или статус недопустим, возвращает False.

## Технологии
1. **Python 3.9+**
- Основной язык программирования, используемый для разработки проекта.
2. **Объектно-ориентированное программирование (ООП)**
- Использование классов Book, LibraryService и CLI для управления данными. Методы классов реализуют основные операции (добавление, удаление, изменение статуса и просмотр книг).
3. **Консольный интерфейс (CLI)**
- Интерфейс взаимодействия с пользователем через терминал для выполнения команд.
4. **Модульное тестирование**
- unittest — библиотека для написания и выполнения тестов, обеспечивающая проверку работоспособности основных функций.  
- unittest.mock — для создания моков (поддельных объектов), используемых в тестах.

## Как установить и запустить
1. Клонирование репозитория
  ```sh
  git clone https://github.com/Dina-Tolkina/Test-task-Development-of-a-library-management-system-.git
  ```
2. Запуск проекта  
   Запустить консольный интерфейс:
  ```sh
  python main.py
  ```
3. Взаимодействие через CLI  
   Следуйте инструкциям, отображаемым в консоли:
- Вводите номера пунктов меню.
- Выполняйте действия (например, добавление, удаление или просмотр книг).

## Тестирование
В проекте реализованы автоматические тесты с использованием библиотеки unittest для проверки основных функций приложения. 
Эти тесты охватывают добавление, удаление, изменение статуса книг, а также просмотр их списка. 
Модуль TestCLI предназначен для тестирования работы консольного интерфейса (CLI) и его корректного взаимодействия с сервисом управления библиотекой (LibraryService).

### Описание тестов:
1. **test_add_book**: Тестирование добавления книги  
   Проверяет, что книга добавляется корректно.
- Эмулируется ввод данных о книге: название, автор, год издания.
- Проверяется, что метод add_book у LibraryService вызывается с правильными параметрами.
- Удостоверяется, что интерфейс выводит подтверждение успешного добавления книги.
2. **test_remove_book**: Тестирование удаления книги  
  Проверяет функциональность удаления книги.
- Эмулируется ввод ID книги для удаления.
- Проверяется, что метод remove_book вызывается с корректным ID.
- Удостоверяется, что интерфейс выводит сообщение об успешном удалении книги.
3. **test_view_all_books**: Тестирование просмотра всех книг  
  Проверяет, что интерфейс корректно отображает список книг.
- Эмулируется возврат списка книг из LibraryService.
- Проверяется, что вывод консоли содержит информацию о каждой книге.
4. **test_change_book_status**: Тестирование изменения статуса книги  
  Проверяет, что изменение статуса книги работает корректно.
  - Эмулируется ввод ID книги и нового статуса.
  - Проверяется, что метод change_book_status вызывается с правильными параметрами.
  - Удостоверяется, что интерфейс выводит подтверждение успешного изменения статуса.
5. **test_invalid_option**: Тестирование обработки неверного выбора  
Проверяет, что консольный интерфейс корректно реагирует на неверный ввод.
- Эмулируется ввод недопустимого пункта меню.
- Проверяется, что интерфейс выводит сообщение об ошибке выбора.

### Запуск тестов
  ```sh
  python -m unittest discover tests/
  ```
