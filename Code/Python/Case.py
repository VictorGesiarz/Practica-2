
class Case:


    def __init__(self, 
                    title: str, 
                    author: str,
                #  publication_year: int,
                    pages: int, 
                    genres: list[str],
                #  bestseller: str,
                #  film: str,
                #  saga: str
                    ) -> None:

        self.title = title
        self.author = author
        # self.publication_year = publication_year
        self.pages = pages
        self.genres = genres
        # self.bestseller = bestseller
        # self.film = film
        # self.saga = saga

        self.transform_to_numbers()


    def __repr__(self) -> str:
        line1 = f'Book name: {self.title}, written by: {self.author}. Has {self.pages} pages and the genres are {", ".join(self.genres)}\n'
        # line2 = f'The vector representatio of this book is: {self.vector}\n'
        return line1


    def transform_to_numbers(self):
        vector = []
        vector.append()        
        return vector
