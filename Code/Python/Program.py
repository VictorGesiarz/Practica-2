
from CBR import CBR
from User import User, UserInteraction
from Case import Case
from Book import Book
from Others import MessagePrinter, LoadData
from Constants import *


class Program():
    
    def __init__(self, path_cases, path_books, path_users, path_texts) -> None:
        self.path_cases = path_cases
        self.path_users = path_users
        
        self.MP = MessagePrinter(LoadData.load_json(path_texts))
        self.UI = UserInteraction(self.MP)
        
        title = LoadData.load_title_txt("./Code/Data/Texts/title.txt")
        print(self.MP.h(title, fill=False))
    
        self.cases = LoadData.load_cases(path_cases)
        self.books = LoadData.load_books(path_books)
        self.users = LoadData.load_users(path_users)
        # self.user = self.UI.init_user(self.users)
        self.user = User()
        
        self.CBR = CBR(self.cases, self.books, self.user, self.MP)
        
        
    def main_loop(self):

        antiquity, pages, genres, bestseller, film, saga = self.UI.ask_questions()
        new_case = Case("", "", antiquity=antiquity, pages=pages, genres=genres, bestseller=bestseller, film=film, saga=saga, user_age=20)
        # new_case = Case("", "", "1 - 2 years", "300 - 600 pages", [COMEDY, ADVENTURE, FANTASY], "No", "No", "Yes", 25)
        print(new_case)
        self.CBR.run(new_case)

        self.cases = self.CBR.cases
        self.end()
        
    
    def end(self):
        LoadData.write_data(self.cases, self.users, path_users=self.path_users, path_cases=self.path_cases)
        end = self.MP.read("Titles", "End")
        print(self.MP.h1(end))
        title = LoadData.load_title_txt("./Code/Data/Texts/bye.txt")
        print(self.MP.h(title, fill=False, padding=1))


P = Program("./Code/Data/cases.csv", "./Code/Data/Books.csv", "./Code/Data/users.csv", "./Code/Data/Texts/texts.json")
P.main_loop()
