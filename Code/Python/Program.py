
from CBR import CBR
from User import User, UserInteraction
from Case import Case
from Others import MessagePrinter, LoadData


class Program():
    
    def __init__(self, path_cases, path_users, path_texts) -> None:
        self.MP = MessagePrinter(LoadData.load_json(path_texts), 158)
        self.UI = UserInteraction(self.MP)
        
        title = LoadData.load_title_txt("./Code/Data/Titles/title5.txt")
        print(self.MP.h(title, fill=False))
    
        self.cases, self.users = LoadData.load_data(path_cases, path_users)
        self.user = self.UI.init_user(self.users)
        
        self.CBR = CBR(self.cases, self.user)
        
        
    def main_loop(self):

        finish = False
        while not finish:
            new_case = self.UI.ask_questions()
        
    
    def end(self):
        end = self.MP.read("Titles", "End")
        print(self.MP.h(end))


P = Program("./Code/Data/cases.csv", "./Code/Data/users.csv", "./Code/Data/texts.json")
P.main_loop()
P.end()
