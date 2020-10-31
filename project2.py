from bs4 import BeautifulSoup
from urllib.request import urlopen as url
import requests
import sys


user_input = input("What recipe are you looking for? " )
source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text

soup = BeautifulSoup(source, 'html.parser')

#Sarticle = soup.find(id='fixed-recipe-card')
#print(article.prettify())
#summary = soup.find_all(class_='fixed-recipe-card__title-link', limit=3)

#prints out the recipe titles and stores the url for the recipe as a variable
for recipe_title in soup.find_all('a',{'class':'fixed-recipe-card__title-link'}, limit=3):
    py1 = (recipe_title['href'])
    print(recipe_title.get_text())
    
py3 = input("Please Pick the number of the recipe which closely matches the recipe that you would like. ")
py2 = source = requests.get (py1) #url of first site url in recipe_title


#writes to file. Currently writes the full html if you type 1 at the end
if py3 == '1':
    sys.stdout = open('output.txt', "wt")
    print(py2.text)
