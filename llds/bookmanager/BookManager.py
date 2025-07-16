#List of books, list of Genre of books and book ratings was given, all list were of equal length.
#book[], genre[], rating[] of equal length n
##Now there were 2 methods which we need to implement,
#1. getHighestRatingBookByGenre("Genre_name") If same rating books then lexographical order
#2. updateBookRatingbyBookName("book_name", int rating)
from collections import defaultdict
from typing import Dict,List
class Book:
    def __init__(self,name:str,genre:str,rating:int):
        self.name = name
        self.genre = genre
        self.rating = rating



class BookStore:
    def __init__(self,books:list[str],genres:list[str],ratings:list[int]):
        n = len(books)
        self.genres_map:Dict[str,List[Book]] = defaultdict(list[Book]) #genres to book
        self.book_map:Dict[str,Book] = defaultdict(Book) #book to book
        for name,genre,rating in zip(books,genres,ratings):
            book = Book(name,genre,rating)
            self.book_map[name] = book
            self.genres_map[genre].append(book)
    def printBook(self):
        print(self.book_map.items())

    def getHighestRatingBookByGenre(self,genre:str) -> str:
        if genre not in self.genres_map:
            raise ValueError("Not element found")
        else:
            best_book = sorted(self.genres_map[genre],key=lambda b:(-b.rating,b.name))[0]
            return best_book.name
    def updateBookRatingbyBookName(self,name:str,rating:int):
        if name in self.book_map:
            self.book_map[name].rating = rating

books = ["BookA", "BookB", "BookC", "BookD"]
genres = ["SciFi", "SciFi", "Fantasy", "Fantasy"]
ratings = [4, 5, 5, 5]

store = BookStore(books, genres, ratings)
store.printBook()

print(store.getHighestRatingBookByGenre("SciFi"))   # Output: BookB
print(store.getHighestRatingBookByGenre("Fantasy")) # Output: BookC (lex order tie-break)

store.updateBookRatingbyBookName("BookA", 6)
print(store.getHighestRatingBookByGenre("SciFi"))   # Output: BookA (after update)