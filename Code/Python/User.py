import hashlib
import getpass

from rich import print
from rich.console import Console

C = Console()
C.print("HELLO WORLD")
C.print("HELLO WORLD", style="italic")


class User:
    
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
    
    
class UserInteraction:
    
    def __init__(self, MP):
        self.MP = MP


    def init_user(self, users: list[User]):
        
        login_title = self.MP.read("Titles", "Login Title")
        print(self.MP.h1(login_title))
        
        login = self.ask_single_choice_question("Login")
        
        if login == "LogIn":
            return self.__login(users)
        elif login == "SignIn":
            return self.__create_user(users)
        elif login == "Continue without identifying":
            return User("NoUser")
    
    
    def __login(self, users: list[User]):

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

        print(self.MP.square("User identified."))

        return identidied_user


    def __create_user(self, users):
        new_user = User()

        username = input("\nEnter a new username: ")
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
        self.MP.square("User created successfully.", "")
        print(new_user, "\n")
        return new_user

    
    def ask_single_choice_question(self, question):
        
        options = self.MP.read("Questions", question, "Options")
        question_name = self.MP.read("Questions", question, "Name")
        question_string = self.MP.read("Questions", question, "Question")
        error_string = self.MP.read("Errors", "Invalid Options")
        
        while True: 
            print(self.MP.h2(question_string))
            print(question_name)
            print(self.MP.l())
            available_options = {num: option for num, option in enumerate(options)}
            for num, option in available_options.items():
                print(f"{num}- {option}")
            print(self.MP.l())
        
            user_input = input()
        
            invalid_options = []
            if user_input.isnumeric():
                user_input = int(user_input)
                if user_input not in available_options.keys():
                    invalid_options.append(user_input)
                else:
                    return available_options[user_input]
            else:
                if user_input in available_options.values():
                    return user_input
                else:
                    invalid_options.append(user_input)
                
            if invalid_options != []:
                print(self.MP.e(error_string, additional_message=", ".join([str(i) for i in invalid_options]), center=False))


    def ask_multiple_choice_question(self, question):

        answer = []
        
        options = self.MP.read("Questions", question, "Options")
        question_name = self.MP.read("Questions", question, "Name")
        question_string = self.MP.read("Questions", question, "Question")
        error_string = self.MP.read("Errors", "Invalid Options")

        finish = False
        while not finish: 
            print(self.MP.h2(question_string))
            print(question_name)
            print(self.MP.l())
            available_options = {num: option for num, option in enumerate(options) if option not in answer}
            for num, option in available_options.items():
                print(f"{num}- {option}")
            print(self.MP.l())

            user_input = input().split()
            
            invalid_options = []
            for i in user_input:
                if i.isnumeric():
                    i = int(i)
                    if i not in available_options.keys():
                        invalid_options.append(i)
                    elif i == len(options) - 1 and len(answer) > 0: 
                        finish = True
                        break
                    else:
                        answer.append(options[i])
                else: 
                    if i in available_options.values():
                        answer.append(i)
                    else:
                        invalid_options.append(i)

            if invalid_options != []:
                print(self.MP.e(error_string, additional_message=", ".join([str(i) for i in invalid_options]), center=False))

            if len(answer) > 0 and "No more" not in options: options = options + ["No more"]

        return answer


    def ask_range_question(self, question):
        ...
        
    def ask_open_question(self, question):
        ...