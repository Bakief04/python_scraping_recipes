from bs4 import BeautifulSoup
from urllib.request import urlopen as url
import requests

user_input = input("What recipe are you looking for? " )
source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text

soup = BeautifulSoup(source, 'html.parser')

#Sarticle = soup.find(id='fixed-recipe-card')
#print(article.prettify())
summary = soup.find_all('div', class_='grid-card-image-container', limit=3)
print(summary)
