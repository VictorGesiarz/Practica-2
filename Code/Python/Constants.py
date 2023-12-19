YEAR = 2023

ANTIQUITY = ["Recently published", "1 - 2 years", "3 - 10 years", "10 - 50 years", "More than 50 years"]

PAGES = ["0 - 100 pages", "100 - 300 pages", "300 - 600 pages", "More than 600 pages", "Unknown"]

GENRES = [
    'speculative', 'science', 'fantasy', 'childrens', 'suspense', 'crime', 'thriller', 'historical',
    'young adult', 'horror', 'romance', 'detective', 'adventure', 'spy', 'alternate', 'satire',
    'gothic', 'techno', 'war', 'sword', 'humour', 'sorcery', 'dystopia', 'utopian', 'high',
    'picture book', 'western', 'military', 'black', 'time travel', 'apocalyptic', 'hard', 'magic',
    'realism', 'steampunk', 'literary', 'epistolary', 'drama', 'erotic', 'vampire', 'cyberpunk',
    'true', 'epic', 'comedy', 'mystery'
]


# ----------------------------------------------------------------------------------------------------------------


import shutil
terminal_size = shutil.get_terminal_size()
terminal_width = terminal_size.columns
terminal_height = terminal_size.lines


P_WIDTH = 75
H_WIDTH = 158
H1_WIDTH = 125
H2_WIDTH = 100
E_WIDTH = P_WIDTH
MAX_WIDTH = terminal_width


# Adaptado al tamaño de un documento word
# P_WIDTH = 50
# H_WIDTH = 158
# H1_WIDTH = 100
# H2_WIDTH = 75
# E_WIDTH = P_WIDTH
# MAX_WIDTH = 100