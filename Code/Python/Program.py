import sys
import os
current_file_path = os.path.abspath(__file__)
code_directory = os.path.abspath(os.path.join(current_file_path, '..', '..'))
os.chdir(code_directory)
sys.path.append(code_directory)


from Python.CBR import CBR
from Python.User import User, UserInteraction
from Python.Case import Case
from Python.Book import Book
from Python.Others import MessagePrinter, LoadData
from Python.Constants import *
from Python.Clusters import Clusters



class Program():
    
    def __init__(self, path_cases, path_books, path_users, path_texts, path_cluster) -> None:
        self.path_cases = path_cases
        self.path_users = path_users
        
        self.MP = MessagePrinter(LoadData.load_json(path_texts))
        self.UI = UserInteraction(self.MP)
        
        title = LoadData.load_title_txt("./Data/Texts/title.txt")
        print(self.MP.h(title, fill=False))
    
        self.cases, count = LoadData.load_cases(path_cases)
        self.books = LoadData.load_books(path_books)
        self.users = LoadData.load_users(path_users)
        # self.user = self.UI.init_user(self.users)
        self.user = User()

        self.clusters = Clusters(self.cases, count, path_cluster, train_on_innit=False)
        
        self.CBR = CBR(self.clusters, self.books, self.user, self.UI)
        
        
    def main_loop(self):
        antiquity, pages, genres, bestseller, film, saga = self.UI.ask_questions()
        new_case = Case("", "", antiquity=antiquity, pages=pages, genres=genres, bestseller=bestseller, film=film, saga=saga, user_age=20)
        self.cluster = self.CBR.run(new_case)
        self.end()
        
    
    def end(self):
        self.cases, count = self.clusters.return_cases()
        LoadData.write_cases(self.cases, count, path_cases=self.path_cases)
        LoadData.write_users(self.users, path_users=self.path_users)
        
        end = self.MP.read("Titles", "End")
        print(self.MP.h1(end))
        title = LoadData.load_title_txt("./Data/Texts/bye.txt")
        print(self.MP.h(title, fill=False, padding=1))


P = Program(
    "./Data/cases.csv", 
    "./Data/Books.csv", 
    "./Data/users.csv", 
    "./Data/Texts/texts.json",
    "./Data/clustering.pkl"
)

P.main_loop()
