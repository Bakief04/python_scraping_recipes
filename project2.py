from bs4 import BeautifulSoup
import requests

user_input = input("What recipe are you looking for?" )
source = requests.get ('https://www.allrecipes.com/search/?wt={}'.format(user_input)).text

soup = BeautifulSoup(source, 'html.parser')

print (soup.prettify())