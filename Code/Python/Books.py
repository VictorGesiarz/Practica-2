
GENRES = ['Romance', 'Terror', 'Fantasy', 'SF']

class Book():

    def __init__(self, title: str, author: str, pages: int, genres: list) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.genres = genres

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
