import json
import textwrap
import pandas as pd
from ast import literal_eval
from User import User
from Case import Case



class LoadData:
    
    @staticmethod
    def load_data(path_cases = "./Code/Python/Data/cases.csv", path_users = "./Code/Python/Data/users.csv",):
        users_db = pd.read_csv(path_users)
        users_list = users_db.values.tolist()
        users = []
        for i in users_list:
            users.append(User(i[0], str(i[1]), i[2], i[3], literal_eval(i[4])))

        cases_db = pd.read_csv(path_cases)
        cases_list = cases_db.values.tolist()
        cases = []
        for i in cases_list:
            cases.append(Case(i[0], i[1], i[2], literal_eval(i[3])))
            
        return cases, users
    
    @staticmethod
    def write_data(cases, users, path_cases = "./Code/Python/Data/cases.csv", path_users = "./Code/Python/Data/users.csv"):
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
    def load_json(filename = "./Code/Python/Data/texts.json"):
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                return json.loads(file.read())
        except FileNotFoundError:
            print("Error: Messages file not found.")
            return {}
        


class MessagePrinter:
    
    def __init__(self, messages, 
                 h_w = 150, h1_w = 100, h2_w = 75, e_w = 50, p_w = 50, l_w = 50,
                 h_p = 3, h1_p = 2, h2_p = 1, e_p = 1, p_p = 0, l_p = 0):
        
        self.__messages = messages
        

    def l(self, style = "l", width=50):
        line = self.__messages["Lines"][style] * self.__widths[width]
        return line + "\n"
        
        
    def read(self, *path):
        message = self.__messages.copy()
        for i in path:
            message = message[i]
        return message


    def p(self, message, additional_message=False, width=50, padding=0, center=True):
        padding = "\n" * padding
        if additional_message:
            message = message.replace(r"{}", additional_message)
        if center:
            lines = message.split("\n")
            messages = []
            for line in lines:
                messages.append(self._center_and_wrap(line, width))
            return padding + "\n".join(messages) + "\n" + padding
        return padding + message + "\n" + padding
        
    
    def p_l(self, message, additional_message=False, style="l", width=50, padding=0, p_padding=0, center=True):
        border = self.l(style=style, width=width)
        message = self.p(message, additional_message=additional_message, width=width, padding=p_padding, center=center)
        padding = "\n" * padding
        line1 = (f"{border}")
        line2 = (f"{message}")
        line3 = (f"{border}")
        return padding + line1 + line2 + line3 + padding
        

    def h1(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="h1", width=100, padding=2, p_padding=1, center=center)


    def h2(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="h2", width=75, padding=1, center=center)
    
    
    def e(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="e", width=50, padding=1, center=center)


    def square(self, message, additional_massage=False, style="s", width=50, padding=1, p_padding=1, center=True):
        padding = "\n" * padding
        p_padding = "\n" * p_padding
        border_style = self.__messages["Lines"][style]

        message = self.p(message, additional_message=additional_massage, width=width, padding=p_padding, center=center)
        messages = message.split("\n")
        message = ""
        for i in messages:
            message += border_style[3] + i + border_style[3] + "\n"
        message = p_padding + message + p_padding

        border = border_style[0] * width
        line1 = (f"{border_style[1]}{border}{border_style[2]}\n")
        line2 = (f"{message}")
        line3 = (f"{border_style[4]}{border}{border_style[5]}\n")
        
        return padding + line1 + line2 + line3 + padding

    
    def h(self, message, additional_message=False, center=True):
        message = self.p(message, additional_message=additional_message, width="h", center=center)
        border_style = self.__messages["Lines"]["h"]
        border = border_style[0] * (self.__widths["h"])
        padding = "\n" * self.__paddings["h"]
        line1 = (f"{border_style[1]}{border}{border_style[2]}\n")
        line2 = (f"\n{message}\n")
        line3 = (f"\n{border_style[3]}{border}{border_style[4]}")
        return padding + line1 + line2 + line3 + padding
    
        
    def _center_and_wrap(self, message, width):
        wrapped_message = textwrap.fill(message, width=width)
        centered_lines = [line.center(width) for line in wrapped_message.splitlines()]
        centered_and_wrapped_message = "\n".join(centered_lines)
        return centered_and_wrapped_message