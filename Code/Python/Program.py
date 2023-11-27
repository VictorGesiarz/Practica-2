
from CBR import CBR
from User import User, Authentication
from Books import Book, cases


new_case = Book("", "I dont know", 200, ["Romance", "Terror"])

Sistem = CBR(cases)
print(Sistem)
Sistem.run(new_case)
print(Sistem)


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
        

