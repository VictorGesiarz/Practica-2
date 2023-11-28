
from CBR import CBR
from User import User, Authentication
from Books import Book
import pandas as pd



class Program():
    
    def __init__(self, cases, users) -> None:
        
        print("- - - - - - - - - - - - - - - - Welcome to the BookFinder! - - - - - - - - - - - - - - - - \n\n")
        
        self.sistem = CBR(cases)
        self.users = users
        self.user = self._init_user_()
        
    def _init_user_(self):
        login = int(input(("Do you want to LogIn (1) or SignIn (2)? ")))
        
        if login == 1:
            return Authentication.login(self.users)
        else:
            return Authentication.create_user(self.users)
        
    def main_loop(self):
        ...
