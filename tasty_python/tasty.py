import requests
from bs4 import BeautifulSoup

baseUrl = 'https://tasty.co/'

class Recipe:
    
    def __init__(self, name, ingredients, preparation, url):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.url = url

class RecipeSearchResult:

    def __init__(self, key, full_name, url):
        self.key = key
        self.full_name = full_name
        self.url = url

def find_reciepes(query):
    searchUrl = 'search?q='
    query = __encode_space(query)
    result_page = requests.get(baseUrl + searchUrl + query)
    
    soup = BeautifulSoup(result_page.text, 'html.parser')
    page_items_list = soup.find_all(
        attrs={"data-vars-object-type": "recipe", "class": "feed-item analyt-unit-tap"})
    recipes_list = []

    for item in page_items_list:
        recipe = RecipeSearchResult(
            item['data-vars-object-name'],
            item.find("div", class_="item-title").string,
            item['href']
        )
        recipes_list.append(recipe)
    return recipes_list

def __encode_space(query):
    return query.replace(' ', '+')