

class User():
    
    def __init__(self, 
                 username:str = "", 
                 password: str = "", 
                 name: str = "", 
                 surname: str = "", 
                 gmail: str = "", 
                 number: int = 0, 
                 gender: str = "", 
                 age: int = 0, 
                 books_read: list = []) -> None:
                 
        self.username = username
        self.password = password
        
        self.name = name
        self.surname = surname
        self.gmail = gmail
        self.number = number
        self.gender = gender
        self.age = age
        
        self.books_read = books_read
        
        
        
class Authentication:
    @staticmethod
    def login(users):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in users:
            if user.username == username and user.password == password:
                return user

        print("Invalid username or password.")
        return None

    @staticmethod
    def create_user(users):
        new_user = User()
        new_user.username = input("Enter a new username: ")
        new_user.password = input("Enter a password: ")
        # ... (other user attribute inputs)

        users.append(new_user)
        print("User created successfully.")
        return new_user