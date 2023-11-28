from Program import Program
from Books import Book
from User import User
import pandas as pd


users_db = pd.read_csv("./Code/Python/Data/users.csv")
users_list = users_db.values.tolist()

users = []
for i in users_list:
    users.append(User(i[0], str(i[1]), i[2], i[3], i[4], i[5], i[6], i[7]))


cases_db = pd.read_csv("./Code/Python/Data/cases.csv")
cases_list = cases_db.values.tolist()

cases = []
for i in cases_list:
    users.append(Book(i[0], i[1], i[2], i[3]))


P = Program(cases, users)


# new_case = Book("", "I dont know", 200, ["Romance", "Terror"])