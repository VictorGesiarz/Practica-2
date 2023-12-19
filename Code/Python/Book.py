from typing import List, Optional


class Book:
    pass

class Book:

    def __init__(self, 
                 title: str, 
                 author: str,
                 summary: str,
                 published_date: int,
                 rating_count: int,
                 rating_mean: int,
                 pages: str, 
                 genres: List[str],
                 bestseller: str,
                 film: str,
                 saga: str,
                 followed_by: Optional['Book'] = None,
                 preceeded_by: Optional['Book'] = None,
                 ) -> None:

        self.title = title
        self.author = author
        self.summary = summary
        self.published_date = published_date
        self.pages = pages
        self.genres = genres
        self.bestseller = bestseller
        self.film = film
        self.saga = saga
        self.followed_by = followed_by
        self.preceeded_by = preceeded_by
        self.rating_count = rating_count
        self.rating_mean = rating_mean


    def __repr__(self) -> str:
        line1 = f'Book NAME: {self.title}, written BY: {self.author} and was PUBLISHED in: {self.published_date}. \n'
        line2 = f'Has {self.pages} PAGES and the GENRES are {", ".join(self.genres)}\n'
        line3 = f'Bestseller: {self.bestseller}, FILM: {self.film}, SAGA: {self.saga}. \n\n'
        line4 = f'SUMMARY: {self.summary}\n'
        return line1 + line2 + line3 + line4