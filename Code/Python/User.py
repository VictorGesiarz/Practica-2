import hashlib
import getpass


class User():
    
    def __init__(self, 
                 username:str = "", 
                 password: str = "", 
                 gender: str = "", 
                 age: int = 0, 
                 books_read: list = ["-"]) -> None:
                 
        self.username = username
        self.password = password
    
        self.gender = gender
        self.age = age
        
        self.books_read = books_read
        

    def __repr__(self) -> str:
        line1 = f'Username: {self.username}. Gender: {self.gender}, age: {self.age}.'
        return line1 + '\n'
        

        
class UserAuthentication:
    @staticmethod
    def login(users: list[User]):

        identidied_user = None

        right_user = False
        while not right_user:
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            sha256 = hashlib.sha256()
            sha256.update(password.encode('utf-8'))
            hashed_password = sha256.hexdigest()
            for user in users:
                if user.username == username and user.password == hashed_password:
                    identidied_user = user
                    right_user = True
                    break
            if not right_user:
                print("The username or password was wrong. Try again.")

        book = input("Do you want to add any new books you have read (End with -)? ")
        while book != "None" and book != "-":
            identidied_user.books_read.append(book)
            book = input()
        if book != "None" and book != "-":
            identidied_user.books_read.append(book)   

        print("\nUser identified.\n")

        return identidied_user


    @staticmethod
    def create_user(users):
        new_user = User()

        username = input("Enter a new username: ")
        while username in [user.username for user in users]:
            username = input("Already exists. Enter a new username: ")
        new_user.username = username

        password = getpass.getpass("Enter a password: ")
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        hashed_password = sha256.hexdigest()
        new_user.password = hashed_password
        
        new_user.gender = input("What is your gender? ")
        new_user.age = int(input("What is your age? "))

        book = input("Can you list some books that you have read (or type '-' to finish)? ")
        while book != "None" and book != "-":
            new_user.books_read.append(book)
            book = input()
        if book != "None" and book != "-":
            new_user.books_read.append(book)

        users.append(new_user)
        print("\nUser created successfully.")
        print(new_user, "\n")
        return new_user