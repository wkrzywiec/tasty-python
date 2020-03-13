import requests
from bs4 import BeautifulSoup
import re

baseUrl = 'https://tasty.co/'

class Recipe: 
    def __init__(self, title, ingredients_sections, preparation, url):
        self.title = title
        self.ingredients_sections = ingredients_sections
        self.preparation = preparation
        self.url = url

class IngredientsSection:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

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
    ingredients_sections = __get_ingredients_sections(soup)
    preparation = ''
    return Recipe(title, ingredients_sections, preparation, url)

def __encode_space(query):
    return query.replace(' ', '+')

def  __get_ingredients_sections(soup):
    sections = []
    sections_html = soup.find_all("div", class_="ingredients__section")
    for section_html in sections_html:
        section = __get_single_ingredients_section(section_html)
        sections.append(section)
    return sections

def __get_single_ingredients_section(section_html):
    section_name = section_html.find("p", class_="ingredient-section-name").string
    ingredients = []
    ingredients_html = section_html.find_all("li", class_="ingredient")
    for ingredient_html in ingredients_html:
        ingredient = __extract_formatted_ingredient(ingredient_html)
        ingredients.append(ingredient)
    return IngredientsSection(section_name, ingredients)

def __extract_formatted_ingredient(point_tag):
    ingredient = ''
    
    for child in point_tag:
        s = str(child)
        
        if s.startswith('<span'):
            s = __remove_span_tag(s)
        
        ingredient_part = s.split()
        for part in ingredient_part:
            ingredient = ingredient + part + ' '
    ingredient = re.sub(' , ', ', ', ingredient)
    ingredient = ingredient.strip()
    return ingredient

def __remove_span_tag(s):
    s = s.replace('<!-- -->', '')
    s = s.replace('</span>', '')
    span_tag = re.search('<(.*?)>', s).group(0)
    s = re.sub(span_tag, ' ', s)
    return s


