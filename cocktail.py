#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
def getCocktail(thing):
    cocktail = thing
    parseForURL = cocktail.lower().replace(' ', '-') + '/'
    url = "http://www.liquor.com/recipes/%s" %parseForURL
    req = requests.get(url)
    if req.status_code != 200:
        print("Welp the website doesn't have that I guess")
    else:
        scrapyBoi = BeautifulSoup(req.text, 'html.parser')
        ingredients = scrapyBoi.find('ul', attrs={'id': 'ingredient-list_1-0'})
        steps = scrapyBoi.find('ol', attrs={'id': 'mntl-sc-block_2-0'})
        return [ingredients.text.strip(), steps.text.strip()]