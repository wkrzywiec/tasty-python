import requests
from bs4 import BeautifulSoup

baseUrl = 'https://tasty.co/'

class Recipe:
    
    def __init__(self, title, ingredients, preparation, url):
        self.title = title
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

def get_recipe(url):
    result_page = requests.get(url)
    soup = BeautifulSoup(result_page.text, 'html.parser')

    title = soup.find('h1').string
    ingredients = []
    preparation = ''
    return Recipe(title, ingredients, preparation, url)

def __encode_space(query):
    return query.replace(' ', '+')