import pandas as pd
from typing import List

class Case:

    def __init__(self, 
                    title: str, 
                    author: str,
                    publication_year: int,
                    pages: int, 
                    genres: List[str],
                    bestseller: str,
                    film: str,
                    saga: str,
                    user_age: int = 20
                    ) -> None:

        self.title = title                          # This element is the solution

        self.author = author                        # This elements are part of the problem
        self.publication_year = publication_year
        self.pages = pages
        self.genres = genres
        self.bestseller = bestseller
        self.film = film
        self.saga = saga
        self.user_age = user_age

        self.transform_to_numbers()                 # We recieve the data in strings and some numbers
                                                    # But we want to transform it into numbers to be able to compute distances


    def __repr__(self) -> str:
        line1 = f'Book NAME: {self.title}, written BY: {self.author}. Has {self.pages} PAGES and the GENRES are {", ".join(self.genres)}\n'
        line2 = f'Bestseller: {self.bestseller}, FILM: {self.film}, SAGA: {self.saga}\n\n'
        return line1 + line2
    
    def __len__(self):
        return len(self.get_list())


    def transform_to_numbers(self):
        
        if self.bestseller == "Yes": self.bestseller = 1 
        else: self.bestseller = 0

        if self.film == "Yes": self.film = 1 
        else: self.film = 0
        
        if self.saga == "Yes": self.saga = 1 
        else: self.saga = 0
        



    def get_list(self):
        return [self.publication_year, self.pages, self.bestseller, self.film, self.saga, self.user_age] + self.genres
