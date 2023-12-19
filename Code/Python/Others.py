import sys
import os
current_file_path = os.path.abspath(__file__)
code_directory = os.path.abspath(os.path.join(current_file_path, '..', '..'))
sys.path.append(code_directory)

import json
import textwrap
import numpy as np
import pandas as pd
from ast import literal_eval
from Python.User import User
from Python.Case import Case
from Python.Book import Book
from Python.Constants import *



class LoadData:
    
    @staticmethod
    def load_users(path_users = "./Code/Data/users.csv",):
        users_db = pd.read_csv(path_users)
        users_list = users_db.values.tolist()
        users = []
        for i in users_list:
            users.append(User(i[0], str(i[1]), i[2], i[3], literal_eval(i[4])))
        return users
    

    @staticmethod
    def load_cases(path_cases = "./Code/Data/cluster_cases.csv"):
        cases_db = pd.read_csv(path_cases)
        cases_list = cases_db.values.tolist()
        count = cases_list[0][0]
        cases_list = cases_list[1:]
        cases = []
        for i in cases_list:
            cases.append(Case(title=i[0], 
                              author=i[1], 
                              antiquity=i[2], 
                              genres=literal_eval(i[3]),
                              pages=i[4],
                              bestseller=i[5],
                              film=i[6],
                              saga=i[7], 
                              evaluation_count=float(i[8]),
                              evaluation_mean=float(i[9])))
        return cases, int(float(count))
    

    @staticmethod
    def load_books(path_books = "./Code/Data/books.csv"):
        books_db = pd.read_csv(path_books)
        books_list = books_db.values.tolist()
        books = []
        for i in books_list:
            books.append(Book(title=i[0], 
                              author=i[1], 
                              published_date=i[2],
                              genres=literal_eval(i[3]),
                              summary=i[4],
                              rating_count=i[5],
                              rating_mean=i[6],
                              pages=i[7],
                              bestseller=i[8],
                              film=i[9],
                              saga=i[10],
                              followed_by=i[11],
                              preceeded_by=i[12]))
        return books


    @staticmethod
    def write_cases(cases, count, path_cases = "./Code/Data/cases.csv"):
        cases_columns = ["Title", "Author", "Publication Year", "Genres", "Number of Pages", "Best Seller", "Film", "Saga", "Evaluation count", "Evaluation mean"]
        cases_list = [[count] + [np.nan] * (len(cases_columns) - 1)]
        for case in cases:
            case._transform_to_string()
            cases_list.append([case.title, case.author, case.antiquity, case.genres, case.pages, case.bestseller, case.film, case.saga, case.evaluation_count, case.evaluation_mean])
        cases_df = pd.DataFrame(cases_list, columns=cases_columns)
        cases_df.to_csv(path_cases, index=False)
        
    @staticmethod
    def write_users(users, path_users = "./Code/Data/users.csv"):
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
        

class MessagePrinter:
    
    def __init__(self, messages, center = True):
        
        self.__messages = messages
        self.max_width = MAX_WIDTH
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

        
    def h(self, message, additional_message=False, width=H_WIDTH, padding=3, p_padding=1, fill=True):
        m1 = self.square(message, additional_message=additional_message, style="h", width=width-8, padding=0, p_padding=p_padding, fill=fill, pad=False)
        m2 = self.square(m1, style="h", width=width-4, padding=0, p_padding=0, fill=fill, pad=False)
        m3 = self.square(m2, style="h", width=width, padding=padding, p_padding=0, fill=fill, pad=False)
        return self.t(m3, width=width)


    def h1(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="h1", width=H1_WIDTH, padding=2, p_padding=1, center=center)


    def h2(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="h2", width=H2_WIDTH, padding=1, center=center)
    
    
    def e(self, message, additional_message=False, center=True):
        return self.p_l(message, additional_message=additional_message, style="e", width=E_WIDTH, padding=1, center=center)


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