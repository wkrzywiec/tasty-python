import unittest
import tasty_python.tasty_client as tasty

class TestTastyClient(unittest.TestCase):

    def test_find_pizza_margherita_recipes(self):
        recipes = tasty.find_reciepes('pizza margherita')
        self.assertGreaterEqual(len(recipes), 6)
        
    def test_get_pizza_margherita_by_mario_batali_recipe(self):
        recipe = tasty.get_recipe('https://tasty.co/recipe/pizza-margherita-by-mario-batali')

        for ingredient in recipe.ingredients:
            print(ingredient)

        self.assertEqual(recipe.title, 'Pizza Margherita by Mario Batali')
        self.assertEqual(len(recipe.ingredients), 11)
        self.assertEqual(recipe.ingredients[0], '1 ¼ cups water (300 mL), warm')
        self.assertEqual(recipe.ingredients[1], '¼ oz active dry yeast (10 g), 1 packet')
        self.assertEqual(recipe.ingredients[2], '1 ½ teaspoons sugar')
        self.assertEqual(recipe.ingredients[3], '3 ½ cups all-purpose flour (435 g)')
        self.assertEqual(recipe.ingredients[4], '2 tablespoons salt')
        self.assertEqual(recipe.ingredients[5], '¼ cup extra virgin olive oil (60 mL)')
        self.assertEqual(recipe.ingredients[6], '2 cups tomato (400 g), strained')
        self.assertEqual(recipe.ingredients[7], 'fresh basil')
        self.assertEqual(recipe.ingredients[8], '8 oz fresh mozzarella cheese (225 g)')
        self.assertEqual(recipe.ingredients[9], 'olive oil')
        self.assertEqual(recipe.ingredients[10], 'salt, to taste')
    
if __name__ == '__main__':
    unittest.main()