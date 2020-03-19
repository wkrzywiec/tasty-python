import requests
from bs4 import BeautifulSoup
import re
"""Module responsible for getting recipes from tasty.co
"""

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
    """Finds the list of recipes that are matching the search query
    
    Arguments:
        query {string} -- search query
    
    Returns:
        [list(RecipeSearchResult)] -- list of results (including title, key & url)
    """
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

def get_recipe_by_key(key):
    """Get specific recipe by its key
    
    Arguments:
        key {string} -- Key of the recipe
    
    Returns:
        Recipe -- Full recipe (including title, ingredients & preparation)
    """
    return get_recipe_by_url(baseUrl + 'recipe/' + key)

def get_recipe_by_url(url):
    """Get specific recipe by its url
    
    Arguments:
        key {string} -- URL of the recipe
    
    Returns:
        Recipe -- Full recipe (including title, ingredients & preparation)
    """
    result_page = requests.get(url)
    soup = BeautifulSoup(result_page.text, 'html.parser')
    is_page_valid = __check_if_page_has_recipe(soup)

    if is_page_valid:
        title = soup.find('h1').string
        ingredients_sections = __get_ingredients_sections(soup)
        preparation = __get_preparation_steps(soup)
        return Recipe(title, ingredients_sections, preparation, url)
    return None

def __encode_space(query):
    return query.replace(' ', '+')

def __check_if_page_has_recipe(soup):
    headline = soup.find("h1").string
    if headline == "Oops! We can't find the page you're looking for.":
        return False
    return True

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

def __get_preparation_steps(soup):
    preparation_steps = []
    preparation_html = soup.find("ol", class_="prep-steps")
    preparation_steps_html = preparation_html.find_all("li")
    for i in range(len(preparation_steps_html)):
        prep = str(i + 1) + '. ' + preparation_steps_html[i].string
        preparation_steps.append(prep)
    return preparation_steps