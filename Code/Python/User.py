import sys
import os
current_file_path = os.path.abspath(__file__)
code_directory = os.path.abspath(os.path.join(current_file_path, '..', '..'))
sys.path.append(code_directory)

from Python.Constants import *

import hashlib
import getpass
from typing import List

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


    def init_user(self, users: List[User]):
        
        login_title = self.MP.read("Titles", "Login Title")
        print(self.MP.h1(login_title))
        
        login = self.ask_single_choice_question("Login")
        print()

        if login == "LogIn":
            return self.__login(users)
        elif login == "SignIn":
            return self.__create_user(users)
        elif login == "Continue without identifying":
            return User("NoUser")
    
    
    def __login(self, users: List[User]):

        identidied_user = None

        right_user = False
        while not right_user:
            username = input(self.MP.t(" - Enter your username: "))
            password = getpass.getpass(self.MP.t(" - Enter your password: "))
            sha256 = hashlib.sha256()
            sha256.update(password.encode('utf-8'))
            hashed_password = sha256.hexdigest()
            for user in users:
                if user.username == username and user.password == hashed_password:
                    identidied_user = user
                    right_user = True
                    break
            if not right_user:
                print(self.MP.t("- - - The username or password was wrong. Try again. - - -"))

        book = input(self.MP.t(" - Do you want to add any new books you have read (End with -)? "))
        while book != "None" and book != "-":
            identidied_user.books_read.append(book)
            book = input()
        if book != "None" and book != "-":
            identidied_user.books_read.append(book)   

        print(self.MP.square("User identified."))

        return identidied_user


    def __create_user(self, users):
        new_user = User()

        username = input(self.MP.t(" - Enter a new username: "))
        while username in [user.username for user in users]:
            username = input(self.MP.t(" - - - Already exists. Enter a new username: "))
        new_user.username = username

        password = getpass.getpass(self.MP.t(" - Enter a password: "))
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        hashed_password = sha256.hexdigest()
        new_user.password = hashed_password
        
        new_user.gender = input(self.MP.t(" - What is your gender? "))
        new_user.age = int(input(self.MP.t(" - What is your age? ")))

        book = input(self.MP.t(" - Can you list some books that you have read (or type '-' to finish)? "))
        while book != "None" and book != "-":
            new_user.books_read.append(book)
            book = input()
        if book != "None" and book != "-":
            new_user.books_read.append(book)

        users.append(new_user)
        self.MP.square("User created successfully.")
        print(new_user, "\n")
        return new_user

    
    def ask_single_choice_question(self, question):
        
        options = self.MP.read("Questions", question, "Options")
        question_string = self.MP.read("Questions", question, "Question")
        error_string = self.MP.read("Errors", "Invalid Options")
        
        while True: 
            print(self.MP.h2(question_string))
            print(self.MP.p(question))
            print(self.MP.l())
            available_options = {num: option for num, option in enumerate(options)}
            for num, option in available_options.items():
                print(self.MP.p(f"{num} - {option}"))
            print(self.MP.l())
        
            user_input = input(self.MP.t())
            print()

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
        
        options = self.MP.read("Questions", question, "Options") + ["No More"]
        question_string = self.MP.read("Questions", question, "Question")
        question_range = self.MP.read("Questions", question, "Range")
        missing_options = self.MP.read("Errors", "Missing Options")
        error_string = self.MP.read("Errors", "Invalid Options")

        if question_range: question_string += f' Select between {question_range[0]} and {question_range[1]}'

        finish = False
        while not finish: 
            print(self.MP.h2(question_string))
            print(self.MP.p(question))
            print(self.MP.l())
            available_options = {num: option for num, option in enumerate(options) if option not in answer}
            for num, option in available_options.items():
                print(self.MP.p(f"{num} - {option}"))
            print(self.MP.l())

            user_input = input(self.MP.t()).split()
            print()
            
            invalid_options = []
            for i in user_input:
                if i.isnumeric():
                    i = int(i)
                    if i not in available_options.keys():
                        invalid_options.append(i)
                    elif i == len(options) - 1: 
                        if len(answer) < question_range[0]:
                            print(self.MP.e(missing_options, additional_message=str(question_range[0]), center=False))                  
                        else:
                            finish = True
                            break
                    else:
                        answer.append(options[i])
                    
                    if len(answer) >= question_range[1]:
                        finish = True
                        break
                else: 
                    if i in available_options.values():
                        answer.append(i)
                    else:
                        invalid_options.append(i)

            if invalid_options != []:
                print(self.MP.e(error_string, additional_message=", ".join([str(i) for i in invalid_options]), center=False))

        print(self.MP.p(f'Chosen options: {" / ".join(answer)}'))
        print()
        return answer


    def ask_range_question(self, question, additional_message=""):
        
        while True:
            question_string = self.MP.read("Questions", question, "Question")
            question_range = self.MP.read("Questions", question, "Range")
            error_string = self.MP.read("Errors", "Invalid Options")
            answer = input(self.MP.p(question_string, additional_message=additional_message, padding=1, width=H2_WIDTH))
            
            if answer.isnumeric():
                answer = int(answer)

                if question_range[0] <= answer <= question_range[1]:
                    return answer
                
            print(self.MP.e(error_string, additional_message=answer, center=False))
        
        
    def ask_question(self, question): 
        question_type = self.MP.read("Questions", question, "Type")
        
        if question_type == "Single Choice":
            return self.ask_single_choice_question(question)
        elif question_type == "Multiple Choice":
            return self.ask_multiple_choice_question(question)
        elif question_type == "Range":
            return self.ask_range_question(question)
        

    def ask_questions(self):
        questions_title = self.MP.read("Titles", "Questions Title")
        print(self.MP.h1(questions_title))
        
        antiquity   = self.ask_question("Publication Year")
        pages       = self.ask_question("Pages")
        genres      = self.ask_question("Genres")
        bestseller  = self.ask_question("Bestseller")
        film        = self.ask_question("Film")
        saga        = self.ask_question("Saga")

        return antiquity, pages, genres, bestseller, film, saga
