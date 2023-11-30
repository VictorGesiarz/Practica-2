
from CBR import CBR
from User import User, UserAuthentication
from Case import Case
from Questions import UserInteraction
import pandas as pd
from ast import literal_eval



class Program():
    
    def __init__(self, path_cases = "./Code/Python/Data/cases.csv", path_users = "./Code/Python/Data/users.csv") -> None:
        
        print("\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("- - - - - - - - - - - - - - - - - - Welcome to the BookFinder! - - - - - - - - - - - - - - - - - - - ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n\n")
        
        self.path_cases = path_cases
        self.path_users = path_users
        
        self.cases, self.users = self._load_data_()
        self.user = self._init_user_()
        
        self.sistem = CBR(self.cases, self.user)
       
        
    def _load_data_(self):
        users_db = pd.read_csv(self.path_users)
        users_list = users_db.values.tolist()
        users = []
        for i in users_list:
            users.append(User(i[0], str(i[1]), i[2], i[3], literal_eval(i[4])))

        cases_db = pd.read_csv(self.path_cases)
        cases_list = cases_db.values.tolist()
        cases = []
        for i in cases_list:
            cases.append(Case(i[0], i[1], i[2], literal_eval(i[3])))
            
        return cases, users
    
    
    def _init_user_(self):
        login = int(input(("Do you want to LogIn (1), SignIn (2) or continue without identifying (3)? ")))
        
        if login == 1:
            user = UserAuthentication.login(self.users)
        elif login == 2:
            user = UserAuthentication.create_user(self.users)
        elif login == 3:
            return User("NoUser")
        return user
        
        
    def main_loop(self):
        ...
        
    
    def end(self):
        cases_list = []
        for case in self.cases:
            cases_list.append([case.title, case.author, case.pages, case.genres])
        cases_columns = ["Title", "Author", "Pages", "Genres"]
        cases_df = pd.DataFrame(cases_list, columns=cases_columns)
        cases_df.to_csv(self.path_cases, index=False)
        
        users_list = []
        for user in self.users:
            users_list.append([user.username, user.password, user.gender, user.age, user.books_read])
        users_columns = ["Username", "Password", "Gender", "Age", "Books Read"]
        users_df = pd.DataFrame(users_list, columns=users_columns)
        users_df.to_csv(self.path_users, index=False)
        
        print("\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("- - - - - - - - - - - - - - - - Thank you for using our recommender! - - - - - - - - - - - - - - - -")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n")


P = Program()
P.end()