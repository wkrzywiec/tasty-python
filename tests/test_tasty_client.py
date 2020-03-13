import unittest
import tasty_python.tasty_client as tasty

class TestTastyClient(unittest.TestCase):

    def test_find_pizza_margherita_recipes(self):
        recipes = tasty.find_reciepes('pizza margherita')
        self.assertGreaterEqual(len(recipes), 6)
        
    def test_get_pizza_margherita_by_mario_batali_recipe(self):
        recipe = tasty.get_recipe('https://tasty.co/recipe/pizza-margherita-by-mario-batali')

        self.assertEqual(recipe.title, 'Pizza Margherita by Mario Batali')
        self.assertEqual(len(recipe.ingredients_sections), 2)

        dough_ingredients_section = recipe.ingredients_sections[0]
        self.assertEqual(dough_ingredients_section.name, 'Dough')
        self.assertEqual(len(dough_ingredients_section.ingredients), 6)
        self.assertEqual(dough_ingredients_section.ingredients[0], '1 ¼ cups water (300 mL), warm')
        self.assertEqual(dough_ingredients_section.ingredients[1], '¼ oz active dry yeast (10 g), 1 packet')
        self.assertEqual(dough_ingredients_section.ingredients[2], '1 ½ teaspoons sugar')
        self.assertEqual(dough_ingredients_section.ingredients[3], '3 ½ cups all-purpose flour (435 g)')
        self.assertEqual(dough_ingredients_section.ingredients[4], '2 tablespoons salt')
        self.assertEqual(dough_ingredients_section.ingredients[5], '¼ cup extra virgin olive oil (60 mL)')

        topping_ingredients_section = recipe.ingredients_sections[1]
        self.assertEqual(topping_ingredients_section.name, 'Topping')
        self.assertEqual(len(topping_ingredients_section.ingredients), 5)
        self.assertEqual(topping_ingredients_section.ingredients[0], '2 cups tomato (400 g), strained')
        self.assertEqual(topping_ingredients_section.ingredients[1], 'fresh basil')
        self.assertEqual(topping_ingredients_section.ingredients[2], '8 oz fresh mozzarella cheese (225 g)')
        self.assertEqual(topping_ingredients_section.ingredients[3], 'olive oil')
        self.assertEqual(topping_ingredients_section.ingredients[4], 'salt, to taste')
    
if __name__ == '__main__':
    unittest.main()