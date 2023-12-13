import json
import textwrap
import pandas as pd
from ast import literal_eval
from User import User
from Case import Case



class LoadData:
    
    @staticmethod
    def load_data(path_cases = "./Code/Data/cases.csv", path_users = "./Code/Data/users.csv",):
        users_db = pd.read_csv(path_users)
        users_list = users_db.values.tolist()
        users = []
        for i in users_list:
            users.append(User(i[0], str(i[1]), i[2], i[3], literal_eval(i[4])))

        cases_db = pd.read_csv(path_cases)
        cases_list = cases_db.values.tolist()
        cases = []
        for i in cases_list:
            cases.append(Case(title=i[0], 
                              author=i[1], 
                              publication_year=i[2], 
                              genres=literal_eval(i[3]),
                              pages=i[5],
                              bestseller=i[6],
                              film=i[7],
                              saga=i[8]))
        return cases, users
    
    @staticmethod
    def write_data(cases, users, path_cases = "./Code/Data/cases.csv", path_users = "./Code/Data/users.csv"):
        cases_list = []
        for case in cases:
            cases_list.append([case.title, case.author, case.pages, case.genres])
        cases_columns = ["Title", "Author", "Pages", "Genres"]
        cases_df = pd.DataFrame(cases_list, columns=cases_columns)
        cases_df.to_csv(path_cases, index=False)
        
        users_list = []
        for user in users:
            users_list.append([user.username, user.password, user.gender, user.age, user.books_read])
        users_columns = ["Username", "Password", "Gender", "Age", "Books Read"]
        users_df = pd.DataFrame(users_list, columns=users_columns)
        users_df.to_csv(path_users, index=False)
        
    @staticmethod
    def load_json(filename = "./Code/Data/texts.json"):
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                return json.loads(file.read())
        except FileNotFoundError:
            print("Error: Messages file not found.")
            return {}
        
    @staticmethod
    def load_title_txt(filename = "./Code/Data/title.txt"):
        with open(filename, 'r', encoding="UTF-8") as file:
            all_lines = file.readlines()
        string = "".join(all_lines)
        return string
        


P_WIDTH = 75
class MessagePrinter:
    
    def __init__(self, messages, max_width = 158, center = True):
        
        self.__messages = messages
        self.max_width = max_width
        self.center_everything = center
        

    def read(self, *path):
        message = self.__messages.copy()
        for i in path:
            message = message[i]
        return message
    

    def t(self, message="", width=P_WIDTH, add_jump=False):
        if self.center_everything:
            remain = (self.max_width - width) // 2
            lines = message.split("\n")
            message = []
            for i in lines:
                message.append(" " * remain + i)
            message = "\n".join(message)
            if add_jump: message += "\n"
        return message


    def l(self, style = "l", width=P_WIDTH, pad=True, add_jump=False):
        line = self.__messages["Lines"][style] * width
        message = line
        if add_jump: message += "\n"
        if pad: return self.t(message, width=width, add_jump=add_jump)
        return message
    

    def p(self, message="", additional_message=False, width=P_WIDTH, padding=0, center=False, fill=True, pad=True, add_jump=False):
        padding = "\n" * padding
        if additional_message:
            message = message.replace(r"{}", additional_message)
        lines = message.split("\n")
        messages = []
        for line in lines:
            messages.append(self.center(line, width, center=center, fill=fill))
        message = padding + "\n".join(messages) + padding
        
        if add_jump: message += "\n"

        if pad: 
            return self.t(message, width=width, add_jump=add_jump)
        return message
        
    
    def p_l(self, message, additional_message=False, style="l", width=P_WIDTH, padding=0, p_padding=0, center=False, fill=True, pad=True):
        border = self.l(style=style, width=width, pad=False, add_jump=True)
        message = self.p(message, additional_message=additional_message, width=width, padding=p_padding, center=center, fill=fill, pad=False, add_jump=True)
        padding = "\n" * padding
        line1 = (f"{border}")
        line2 = (f"{message}")
        line3 = (f"{border}")
        message = padding + line1 + line2 + line3 + padding
        
        if pad: return self.t(message, width=width)
        return message

        
    def h(self, message, additional_message=False, width=158, padding=3, p_padding=1, fill=True):
        m1 = self.square(message, additional_message=additional_message, style="h", width=width-8, padding=0, p_padding=p_padding, fill=fill, pad=False)
        m2 = self.square(m1, style="h", width=width-4, padding=0, p_padding=0, fill=fill, pad=False)
        m3 = self.square(m2, style="h", width=width, padding=padding, p_padding=0, fill=fill, pad=False)
        return m3


    def h1(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="h1", width=125, padding=2, p_padding=1, center=center)


    def h2(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="h2", width=100, padding=1, center=center)
    
    
    def e(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="e", width=P_WIDTH, padding=1, center=center)


    def square(self, message, additional_message=False, style="s", width=35, padding=1, p_padding=0, fill=True, pad=True):
        border_style = self.__messages["Lines"][style]

        padding = "\n" * padding
        p_padding = (border_style[3] + " " * width + border_style[3] + "\n") * p_padding

        message = self.p(message, additional_message=additional_message, width=width, padding=0, center=True, fill=fill, pad=False, add_jump=True)
        messages = message.split("\n")[:-1]
        message = ""
        for i in messages:
            message += border_style[3] + i + border_style[3] + "\n"
        message = p_padding + message + p_padding

        border = border_style[0] * width
        line1 = (f"{border_style[1]}{border}{border_style[2]}\n")
        line2 = (f"{message}")
        line3 = (f"{border_style[4]}{border}{border_style[5]}")
        message = padding + (line1 + line2 + line3) + padding
        
        if pad: return self.t(message, width=width)
        return message
    
        
    def center(self, message, width, center=True, fill=True):
        wrapped_message = message
        if fill:
            wrapped_message = textwrap.fill(message, width=width)
        if center:
            lines = [line.center(width) for line in wrapped_message.splitlines()]
            wrapped_message = "\n".join(lines)
        return wrapped_message