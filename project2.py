from bs4 import BeautifulSoup
from urllib.request import urlopen as url
import requests
import sys
import string
import json

user_input = input("What recipe are you looking for? " )
source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text

soup = BeautifulSoup(source, 'html.parser')

#prints out the recipe titles and stores the url for the recipe as a variable

for recipe_title in soup.find_all('a',{'class':'fixed-recipe-card__title-link'}, limit=3):
    print(recipe_title.get_text())
    
py3 = input("Please type the recipe which closely matches the recipe that you would like. ")
py3 = py3.replace(' ', '-')

#url of first site url in recipe_title

py2 = source = requests.get ("https://www.allrecipes.com/recipe/{}".format(py3)).text
soup2 = soup.find_all({'ul class':'ingredients-section'})
for ingredients in soup.find_all('ul', {'class': 'recipeIngredient'}):
    print(ingredients.get_text())

py4 = input("Are you sure this is correct? ({}) [Y/N]  ".format(py3.replace('-', ' ')))

#writes to file. Currently writes the full html

if py4 == 'Y':
    sys.stdout = open('{}.txt'.format(py3.replace('-', ' ')), 'wt')
    print(py2)