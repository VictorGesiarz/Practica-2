

class User():
    
    def __init__(self, 
                 username:str = "", 
                 password: str = "", 
                 name: str = "", 
                 surname: str = "", 
                 gmail: str = "", 
                 number: int = 0, 
                 gender: str = "", 
                 age: int = 0, 
                 books_read: list = []) -> None:
                 
        self.username = username
        self.password = password
        
        self.name = name
        self.surname = surname
        self.gmail = gmail
        self.number = number
        self.gender = gender
        self.age = age
        
        self.books_read = books_read
        

    def __repr__(self) -> str:
        line1 = f'Username: {self.username}. Full name: {self.name} {self.surname}. Gender: {self.gender}, age: {self.age}.'
        line2 = f'Gmail: {self.gmail}. Number: {self.number}'
        return line1 + line2 + '\n'
        

        
class Authentication:
    @staticmethod
    def login(users: list[User]):

        identidied_user = None

        username = input("Enter your username: ")
        password = input("Enter your password: ")
        right_user = False
        while not right_user:
            for user in users:
                if user.username == username and user.password == password:
                    identidied_user = user
                    right_user = True
                    break

        return identidied_user


    @staticmethod
    def create_user(users):
        new_user = User()

        username = input("Enter a new username: ")
        while username not in [user.username for user in users]:
            username = input("Already exists. Enter a new username: ")
        new_user.username = username

        new_user.password = input("Enter a password: ")
        new_user.name = input("What is your name? ")
        new_user.surname = input("What is your last name? ")
        new_user.gmail = input("What is your gmail? ")
        new_user.number = int(input("What is your number? "))
        new_user.gender = input("What is your gender? ")
        new_user.age = int(input("What is your age? "))

        book = input("Can you list some books that you have read? ")
        while book != None or book != "-":
            new_user.books_read.append(book)
            book = input()
        new_user.books_read.append(book)    

        users.append(new_user)
        print("User created successfully.")
        print(new_user)
        return new_user