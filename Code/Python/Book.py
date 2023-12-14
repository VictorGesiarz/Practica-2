from typing import List, Optional


class Book:
    pass

class Book:

    def __init__(self, 
                 title: str, 
                 author: str,
                 summary: str,
                 published_date: int,
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