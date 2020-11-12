import requests
import json
from bs4 import BeautifulSoup
import sys

while True:
    quit_program = 'quit'
    user_input = input("What recipe are you looking for? (type quit to exit) " )
    if user_input == quit_program:
        sys.exit("thank you for using this program")
    source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text
    soup = BeautifulSoup(source, 'lxml')

#prints out the recipe titles and stores the url for the recipe as a variable
    for recipe_title in soup.find_all('a',{'class':'fixed-recipe-card__title-link'}, limit=3):
        print(recipe_title.get_text())
    py3 = input("What recipe best matches what you are looking for? ")
    py3 = py3.replace(' ', '-')
    url = 'https://www.allrecipes.com/recipe/{}'.format(py3)
    if py3 == quit_program:
        sys.exit('thank you for using the program')
# url for recipe with variable passed in

    r = requests.get(url) 
    soup = BeautifulSoup(r.content, "lxml")

#parses json to treat variable as dictionary
    start = '<script type="application/ld+json">'
    end = '</script>'
    try:
        json_data = r.text[r.text.find(start) + len(start):r.text.find(end)]
        data = json.loads(json_data)[1]
    except json.decoder.JSONDecodeError:
        print("Poorly formatted JSON, please try another recipe")
        break
    confirm = input('Are you sure this is correct?[Y/N] ')
#Writes to file
    try:
        if confirm == ('Y'):
            print('Thank you, The recipe is in a file for easier viewing')
            with open('{}.txt'.format(py3.replace('-', ' ')), 'w+') as file1:
                file1.write('Ingredients')
                file1.write('\n')
                for person in data["recipeIngredient"]:
	                file1.writelines(person + '\n')
                file1.write('\n')
                file1.write('Instructions')
                file1.write('\n')
                for step in data["recipeInstructions"]:
	                file1.writelines(step['text'])
        elif confirm == ('N'):
            print('Run Program to Try Again')
            break
    except UnicodeEncodeError:
        print("Poorly formatted JSON, please try another recipe")
        break
            
    exit_program = input("Would you like to find another recipe? [Y/N] ")
    if exit_program == "N":
        sys.exit('thank you for using the program')
    else: 
        continue