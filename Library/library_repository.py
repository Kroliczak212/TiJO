from abc import ABC, abstractmethod

class LibraryRepository(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int): pass

    @abstractmethod
    def remove_book(self, title: str) -> bool: pass

    @abstractmethod
    def get_all_books(self) -> list: pass

class InMemoryRepository(LibraryRepository):
    def __init__(self):
        self.books = {}

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = {
            'author': author,
            'year': year
        }

    def remove_book(self, title: str) -> bool:
        if title in self.books:
            del self.books[title]
            return True
        return False

    def get_all_books(self) -> list:
        return [{'title': k, **v} for k, v in self.books.items()]
