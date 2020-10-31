from bs4 import BeautifulSoup
from urllib.request import urlopen as url
import requests
import sys


user_input = input("What recipe are you looking for? " )
source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text

soup = BeautifulSoup(source, 'html.parser')

#prints out the recipe titles and stores the url for the recipe as a variable
for recipe_title in soup.find_all('a',{'class':'fixed-recipe-card__title-link'}, limit=3):
    py1 = (recipe_title['href'])
    print(recipe_title.get_text())
    
py3 = input("Please type the recipe which closely matches the recipe that you would like. ")
py2 = source = requests.get ("https://www.allrecipes.com/recipe/{}".format(py3)).text #url of first site url in recipe_title
py4 = input("Are you sure this is correct? [Y/N]  ") 

#writes to file. Currently writes the full html if you type 1 at the end
if py4 == 'Y':
    sys.stdout = open('{}.txt'.format(py3), 'wt')
    print(py2)