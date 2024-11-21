from src.file_storage import FileStorage
from src.repository import Repository
from src.library_service import LibraryService
from src.cli import CLI

def main():
    """Основная функция для запуска приложения."""
    storage = FileStorage("data/books.json")
    repository = Repository(storage)
    library_service = LibraryService(repository)
    cli = CLI(library_service)
    cli.run()

if __name__ == "__main__":
    main()
