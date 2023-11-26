
from CBR import CBR



cases = [
    ["The Hunger Games", "Suzanne Collins", 374, ["fantasy", "science-fiction", "romance"]],
    ["Harry Potter 1", "J.K. Rowling", 194, ["fantasy", "magic"]],
    ["Pride and Prejudice", "Jane Austen", 279, ["historical-fiction", "historical-romance"]],
    ["Twilight", "Stephenie Meyer", 501, ["fantasy", "romance"]],
]


def Manhattan(new_case, case):
    
    """Function to calculate the similarity between two cases. This function performs the Manhattan distance."""

    weights = [1 for _ in range(len(new_case))]

    return sum(abs(new_case[i] - case[i]) * weights[i] for i in range(len(new_case)))



Sistem = CBR(cases, Manhattan)
