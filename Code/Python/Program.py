
from CBR import CBR
from User import User, UserInteraction
from Case import Case
from Others import MessagePrinter, LoadData


class Program():
    
    def __init__(self, path_cases, path_users, path_texts) -> None:
        self.MP = MessagePrinter(LoadData.load_json(path_texts))
        self.UI = UserInteraction(self.MP)
        
        title = self.MP.read("Titles", "Main Title")
        print(self.MP.h(title))
    
        self.cases, self.users = LoadData.load_data(path_cases, path_users)
        self.user = self.UI.init_user(self.users)
        
        self.CBR = CBR(self.cases, self.user)
        
        
    def main_loop(self):
        
        questions_title = self.MP.read("Titles", "Questions Title")
        print(self.MP.h1(questions_title))
        
        self.UI.ask_single_choice_question("Another")
        self.UI.ask_multiple_choice_question("Languages")
        
    
    def end(self):
        end = self.MP.read("Titles", "End")
        print(self.MP.h(end))


P = Program("./Code/Python/Data/cases.csv", "./Code/Python/Data/users.csv", "./Code/Python/Data/texts.json")
P.main_loop()
P.end()
