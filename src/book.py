class Book:
    """Модель книги."""

    def __init__(self, title: str, author: str, year: int, book_id: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status 

    @classmethod
    def from_dict(cls, data: dict):
        """Создать книгу из словаря."""
        return cls(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data.get("status", "в наличии")  
        )

    def change_status(self, status: str) -> None:
        """Изменить статус книги."""
        if status not in ["в наличии", "выдана"]:
            raise ValueError("Неверный статус.")
        self.status = status
