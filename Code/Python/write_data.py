import pandas as pd

users = [
    ["VictorGesiarz", "1234", "Victor", "Gesiarz", "victor.gesiarz@estudiantat.upc.edu", 689425100, "M", 20],
    ["PapaNoelito", "4321", "Noel", "Planell", "noel.planell@estudiantat.upc.edu", 689123425, "F", 45]
]

users_columns = ["Username", "Password", "FirstName", "LastName", "Email", "Phone", "Gender", "Age"]
users_df = pd.DataFrame(users, columns=users_columns)
users_df.to_csv("./Code/Python/Data/users.csv")


cases = [
    ["The Hunger Games", "Suzanne Collins", 374, ["Fantasy", "SF", "Romance"]],
    ["Harry Potter 1", "J.K. Rowling", 194, ["Fantasy", "SF"]],
    ["Pride and Prejudice", "Jane Austen", 279, ["Romance", "Terror"]],
    ["Twilight", "Stephenie Meyer", 501, ["Fantasy", "Romance"]]
]


cases_columns = ["Title", "Author", "Pages", "Genres"]
cases_df = pd.DataFrame(cases, columns=cases_columns)
cases_df.to_csv("./Code/Python/Data/cases.csv")