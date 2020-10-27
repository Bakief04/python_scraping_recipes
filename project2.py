from bs4 import BeautifulSoup
from urllib.request import urlopen as url
import requests

user_input = input("What recipe are you looking for? " )
source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text

soup = BeautifulSoup(source, 'html.parser')

#Sarticle = soup.find(id='fixed-recipe-card')
#print(article.prettify())
#summary = soup.find_all(class_='fixed-recipe-card__title-link', limit=3)
for el in soup.find_all('a',{'class':'fixed-recipe-card__title-link'}, limit=3):
    print(el.get_text())
        #summarylink = (['href'])
    
py1 = input("would you like to get this recipe? ")
#link2 = source = requests.get (summarylink)

#if py1 == 'yes':
 #   print(link2.text)
