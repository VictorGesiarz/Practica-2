
GENRES = 4

class Book():

    def __init__(self, title: str, author: str, pages: int, genres: list) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.genres = genres

        self.vector = self.calculate_vector()


    def __repr__(self) -> str:
        return f'Book name: {self.title}, written by: {self.author}. Has {self.pages} pages and the genres are {", ".join(self.genres)}'

    def calculate_vector(self):
        vector = []

        vector.append(self.pages)

        vector.append(len(self.genres) / GENRES)

        return vector


cases = [
    Book("The Hunger Games", "Suzanne Collins", 374, ["fantasy", "science-fiction", "romance"]),
    Book("Harry Potter 1", "J.K. Rowling", 194, ["fantasy", "magic"]),
    Book("Pride and Prejudice", "Jane Austen", 279, ["historical-fiction", "historical-romance"]),
    Book("Twilight", "Stephenie Meyer", 501, ["fantasy", "romance"]),
]



"""

ESTA IDEA NO ESTA MAL PERO TIENE UN PROBLEMA QUE NO SE COMO CUANTIFICAR CADA UNA DE LAS VARIABLES QUE ENTRAN DENRTO DE UN LIBRO

"""