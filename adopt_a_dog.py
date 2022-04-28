from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals2.aspx?species=Dog&sex=A&agegroup=All&onhold=N&orderby=ID&colnum=3&AuthKey=1w2169r3m576xy6505c6z57e3g07tkl0vwgcx29kkels9bo086&css=https://ws.petango.com/WebServices/adoptablesearch/css/styles.css').text
soup = BeautifulSoup(html_text, 'lxml')
dogs = soup.find_all('div', class_ = 'list-animal-info-block' )

for dog in dogs:

    dogs_type = dog.find('div', class_ = 'list-animal-breed').text

    if 'Chihuahua, Short Coat/Mix' in dogs_type:
        print (dogs_type)
        more_info = dog.a['href']
        print(f"https://ws.petango.com/webservices/adoptablesearch/" + more_info)

    elif 'Chihuahua' in dogs_type:
        print (dogs_type)
        more_info = dog.a['href']
        print(f"https://ws.petango.com/webservices/adoptablesearch/" + more_info)
