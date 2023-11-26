
from CBR import CBR



cases = [
    ["The Hunger Games", "Suzanne Collins", 374, ["fantasy", "science-fiction", "romance"]],
    ["Harry Potter 1", "J.K. Rowling", 194, ["fantasy", "magic"]],
    ["Pride and Prejudice", "Jane Austen", 279, ["historical-fiction", "historical-romance"]],
    ["Twilight", "Stephenie Meyer", 501, ["fantasy", "romance"]],
]


cases2 = [
    [2, 3, 2, 0],
    [2, 2, 1, 1], 
    [4, 3, 2, 2], 
    [0, 0, -1, 0]
]


Sistem = CBR(cases2)
print(Sistem)
Sistem.run([3, 1, 2])
print(Sistem)