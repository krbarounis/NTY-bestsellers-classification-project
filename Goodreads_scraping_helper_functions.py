def get_title(soup):
    title = soup.find('h1',{'id':'bookTitle'}).get_text()
    clean_title = title.replace("\n"," ").replace("  ", "")
    return clean_title

def get_ISBN(soup):
    try:
        ISBN = soup.find_all('div',class_='infoBoxRowItem')[1].get_text()
        clean_ISBN = ISBN.replace("\n"," ").replace("\n"," ").replace(" ", "").split("(")[1].replace(")","").replace("ISBN13:","")
    except IndexError:
        clean_ISBN = ""
    return clean_ISBN

def get_author(soup):
    author = soup.find('span', itemprop='name').get_text()
    return author

def get_series(soup):
    series = soup.find('a',class_='greyText').get_text()
    clean_series = series.replace("\n"," ").replace("  ", "").replace("(","").replace(")","")
    return clean_series

def get_genre(soup):
    try:
        genre = soup.find('a', class_='actionLinkLite bookPageGenreLink')
        clean_genre = genre['href'].replace("/genres/","")
    except TypeError:
        clean_genre = ""
    return clean_genre

def get_rating(soup):
    rating = soup.find('span', itemprop='ratingValue').get_text()
    clean_rating = rating.replace("\n"," ").replace(" ", "")
    return clean_rating

def get_publish_date(soup):
    try:
        date = soup.find_all('div',class_='row')[1].get_text()
        clean_date = date.replace("\n"," ").replace("  ","").split('by')[0].replace(' Published ',"")
    except IndexError:
        clean_date = ""
    return clean_date

def get_publishing_company(soup):
    try:
        company = soup.find_all('div',class_='row')[1].get_text()
        clean_company = company.replace("\n"," ").replace("  ","").split('by ')[1]
    except IndexError:
        clean_company = ""
    return clean_company

def get_pages(soup):
    try:
        pages = soup.find('span', itemprop='numberOfPages').get_text().split()[0]
    except AttributeError:
        pages = ""
    return pages

def get_format(soup):
    try: 
        book_format = soup.find('span',itemprop = 'bookFormat').get_text()
    except AttributeError:
        book_format = ""
    return book_format
