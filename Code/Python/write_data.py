import pandas as pd

users = [
    ['Victor', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'M', 20, ['-']], 
    ['Noel', 'fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3', 'M', 20, ['-']]
]

users_columns = ["Username", "Password", "Gender", "Age", "Books Read"]
users_df = pd.DataFrame(users, columns=users_columns)
users_df.to_csv("./Code/Python/Data/users.csv", index=False)


cases = [
    ["The Hunger Games", "Suzanne Collins", 374, ["Fantasy", "SF", "Romance"]],
    ["Harry Potter 1", "J.K. Rowling", 194, ["Fantasy", "SF"]],
    ["Pride and Prejudice", "Jane Austen", 279, ["Romance", "Terror"]],
    ["Twilight", "Stephenie Meyer", 501, ["Fantasy", "Romance"]]
]


cases_columns = ["Title", "Author", "Pages", "Genres"]
cases_df = pd.DataFrame(cases, columns=cases_columns)
cases_df.to_csv("./Code/Python/Data/cases.csv", index=False)