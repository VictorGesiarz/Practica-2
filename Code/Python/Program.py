
from CBR import CBR
from User import User, UserInteraction
from Case import Case
from Others import MessagePrinter, LoadData
from Constants import *


class Program():
    
    def __init__(self, path_cases, path_users, path_texts) -> None:
        self.MP = MessagePrinter(LoadData.load_json(path_texts), 158)
        self.UI = UserInteraction(self.MP)
        
        title = LoadData.load_title_txt("./Code/Data/Texts/title.txt")
        print(self.MP.h(title, fill=False))
    
        self.cases, self.users = LoadData.load_data(path_cases, path_users)
        # self.user = self.UI.init_user(self.users)
        self.user = User()
        
        self.CBR = CBR(self.cases, self.user)
        
        
    def main_loop(self):

        # finish = False
        # while not finish:
        #     new_case = self.UI.ask_questions()

        new_case = Case("", "", 2000, 350, [COMEDY, ADVENTURE, FANTASY], "No", "No", "Yes", 25)
        self.CBR.run(new_case)
        
    
    def end(self):
        end = self.MP.read("Titles", "End")
        print(self.MP.h(end))


P = Program("./Code/Data/books.csv", "./Code/Data/users.csv", "./Code/Data/Texts/texts.json")
P.main_loop()
P.end()
