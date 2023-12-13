SPECULATIVE     = 'speculative'
SCIENCE         = 'science'
FANTASY         = 'fantasy'
CHILDRENS       = 'childrens'
SUSPENSE        = 'suspense'
CRIME           = 'crime'
THRILLER        = 'thriller'
HISTORICAL      = 'historical'
YOUNG_ADULT     = 'young adult'
HORROR          = 'horror'
ROMANCE         = 'romance'
DETECTIVE       = 'detective'
ADVENTURE       = 'adventure'
SPY             = 'spy'
ALTERNATE       = 'alternate'
SATIRE          = 'satire'
GOTHIC          = 'gothic'
TECHNO          = 'techno'
WAR             = 'war'
SWORD           = 'sword'
HUMOUR          = 'humour'
SORCERY         = 'sorcery'
DYSTOPIA        = 'dystopia'
UTOPIAN         = 'utopian'
HIGH            = 'high'
PICTURE_BOOK    = 'picture book'
WESTERN         = 'western'
MILITARY        = 'military'
BLACK           = 'black'
TIME_TRAVEL     = 'time travel'
APOCALYPTIC     = 'apocalyptic'
HARD            = 'hard'
MAGIC           = 'magic'
REALISM         = 'realism'
STEAMPUNK       = 'steampunk'
LITERARY        = 'literary'
EPISTOLARY      = 'epistolary'
DRAMA           = 'drama'
EROTIC          = 'erotic'
VAMPIRE         = 'vampire'
CYBERPUNK       = 'cyberpunk'
TRUE            = 'true'
EPIC            = 'epic'
COMEDY          = 'comedy'
MYSTERY         = 'mystery'



GENRES = [
    'speculative', 'science', 'fantasy', 'childrens', 'suspense', 'crime', 'thriller', 'historical',
    'young adult', 'horror', 'romance', 'detective', 'adventure', 'spy', 'alternate', 'satire',
    'gothic', 'techno', 'war', 'sword', 'humour', 'sorcery', 'dystopia', 'utopian', 'high',
    'picture book', 'western', 'military', 'black', 'time travel', 'apocalyptic', 'hard', 'magic',
    'realism', 'steampunk', 'literary', 'epistolary', 'drama', 'erotic', 'vampire', 'cyberpunk',
    'true', 'epic', 'comedy', 'mystery'
]

genres_dict = dict(zip(GENRES, range(1, len(GENRES) + 1)))

for key, value in genres_dict.items():
    globals()[key.replace(" ", "_").upper()] = value

