
GENRES = ['Romance', 'Terror', 'Fantasy', 'SF']

class Case():

    def __init__(self, 
                 title: str, 
                 author: str,
                 publication_year: int, 
                 pages: int, 
                 genres: list[str],
                 bestseller: str,
                 film: str,
                 saga: str) -> None:
        
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.pages = pages
        self.genres = genres
        self.bestseller = bestseller
        self.film = film
        self.saga = saga

        self.vector = self.calculate_vector()


    def __repr__(self) -> str:
        line1 = f'Book name: {self.title}, written by: {self.author}. Has {self.pages} pages and the genres are {", ".join(self.genres)}\n'
        # line2 = f'The vector representatio of this book is: {self.vector}\n'
        return line1

    def calculate_vector(self):
        vector = []

        vector.append(self.pages)

        for i in GENRES:
            if i in self.genres:
                vector.append(1)
            else:
                vector.append(0)

        return vector
