import requests
import json
from bs4 import BeautifulSoup
import sys

user_input = input("What recipe are you looking for? (type quit to exit) " )

source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text
soup = BeautifulSoup(source, 'html.parser')

#prints out the recipe titles and stores the url for the recipe as a variable
for recipe_title in soup.find_all('a',{'class':'fixed-recipe-card__title-link'}, limit=3):
    print(recipe_title.get_text())

py3 = input("What recipe best matches what you are looking for? ")
py3 = py3 = py3.replace(' ', '-')
url = 'https://www.allrecipes.com/recipe/{}'.format(py3)

# url for recipe with variable passed in

r = requests.get(url) 
soup = BeautifulSoup(r.content, "html.parser")

#parses json to treat variable as dictionary

start = '<script type="application/ld+json">'
end = '</script>'
json_data = r.text[r.text.find(start) + len(start):r.text.find(end)]
data = json.loads(json_data)[1]

confirm = input('Are you sure this is correct?[Y/N] ')
print('Thank you, The recipe is in a file for easier viewing')
#Writes to file
if confirm == ('Y'):
    test = sys.stdout = open('{}.txt'.format(py3.replace('-', ' ')), 'w+')
    print('Ingredients')
    for person in data['recipeIngredient']:
        print(person)
    print('\n')
    print('Instructions')
    for step in data["recipeInstructions"]:
        print(step['text'])