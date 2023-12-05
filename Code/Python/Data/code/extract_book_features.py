import re
def extract_book_features(soup, infobox_table=None):

    if not infobox_table:
        infobox_table = soup.find('table', class_='infobox')
    
    if not infobox_table:
        return None
    

    # Find if the book is a best seller
    best_seller_words = ['bestseller', 'bestselling'] # We can also detect "bestsellers" "bestsellings"

    content = soup.get_text().lower().replace('-', ' ')
    
    best_seller = False
    film = False

    for word in best_seller_words:
        if word in content:
            best_seller = True
            break
    
    words = content.split()

    if 'film' in words:
        film = True
    elif 'movie' in words:
        film = True

    pages = infobox_table.find('th', string='Pages')

    if pages:
        pages = pages.find_next('td').get_text(strip=True)
        pages = re.sub('[^0-9]', '', pages)
    




    saga = infobox_table.find('th', string='Series')

    if saga:
        saga = saga.find_next('td').get_text(strip=True)

    preceded_by = infobox_table.find('th', string=lambda text: text and re.sub(r'[^a-zA-Z]', '', text) == 'Precededby')

    if preceded_by:
        preceded_by = preceded_by.find_next('td').get_text(strip=True)

    followed_by = infobox_table.find('th', string=lambda text: text and re.sub(r'[^a-zA-Z]', '', text) == 'Followedby')

    if followed_by:
        followed_by = followed_by.find_next('td').text.strip()

    return [pages, best_seller, film, saga, preceded_by, followed_by]