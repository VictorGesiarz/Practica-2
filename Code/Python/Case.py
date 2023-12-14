import pandas as pd
from typing import List, Optional
from Constants import * 


class Case:

    def __init__(self, 
                 title: str, 
                 author: str,
                 antiquity: int,
                 pages: str, 
                 genres: List[str],
                 bestseller: str,
                 film: str,
                 saga: str,
                 evaluation_count: int = 0,
                 evaluation_mean: int = 0,
                 user_age: int = 20
                 ) -> None:

        self.title = title                          # This element is the solution

        self.author = author                        # This elements are part of the problem
        self.antiquity = antiquity
        self.pages = pages
        self.genres = genres
        self.bestseller = bestseller
        self.film = film
        self.saga = saga
        self.user_age = user_age

        self.evaluation_count = evaluation_count
        self.evaluation_mean = evaluation_mean

        self._transform_to_numbers()                 # We recieve the data in strings and some numbers
                                                    # But we want to transform it into numbers to be able to compute distances


    def __repr__(self) -> str:
        line1 = f'Book NAME: {self.title}, written BY: {self.author} and was PUBLISHED: {ANTIQUITY[self.antiquity]}. \nHas {PAGES[self.pages]} PAGES and the GENRES are {", ".join([GENRES[i] for i, genre in enumerate(self.genres) if genre])}\n'
        line2 = f'Bestseller: {self.bestseller}, FILM: {self.film}, SAGA: {self.saga}\n\n'
        return line1 + line2
    

    def _transform_to_numbers(self):
        
        if self.bestseller == "Yes": self.bestseller = 1 
        else: self.bestseller = 0

        if self.film == "Yes": self.film = 1 
        else: self.film = 0
        
        if self.saga == "Yes": self.saga = 1 
        else: self.saga = 0
        

        self.genres = [1 if genre in self.genres else 0 for genre in GENRES]

        self.antiquity = ANTIQUITY.index(self.antiquity)

        self.pages = PAGES.index(self.pages)


    def _transform_to_string(self):
        
        if self.bestseller == 1: self.bestseller = "Yes"
        else: self.bestseller = "No"

        if self.film == 1: self.film = "Yes"
        else: self.film = "No"

        if self.saga == 1: self.saga = "Yes"
        else: self.saga = "No"

        self.genres = [GENRES[i] for i, value in enumerate(self.genres) if value]

        self.antiquity = ANTIQUITY[self.antiquity]

        self.pages = PAGES[self.pages]


    def get_variables(self):
        return [self.antiquity, self.pages, self.bestseller, self.film, self.saga], self.genres


    def copy(self):
        self._transform_to_string()
        case = Case(title=self.title,
                    author=self.author,
                    antiquity=self.antiquity,
                    pages=self.pages,
                    genres=self.genres,
                    bestseller=self.bestseller,
                    film=self.film,
                    saga=self.saga,
                    evaluation_count=self.evaluation_count,
                    evaluation_mean=self.evaluation_mean)
        self._transform_to_numbers()
        return case