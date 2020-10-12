from bs4 import BeautifulSoup
import requests

source = requests.get ('https://webscraper.io/test-sites/e-commerce/allinone').text

soup = BeautifulSoup(source, 'html.parser')

print (soup.prettify())