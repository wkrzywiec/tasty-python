import unittest
import tasty_python.tasty as tasty

class TestTastyClient(unittest.TestCase):

    def test_find_pizza_margherita_recipes(self):
        recipes = tasty.find_reciepes('pizza margherita')

        for recipe in recipes:
            print(recipe.key)
            print(recipe.full_name)
            print(recipe.url)
            print()
        self.assertGreaterEqual(len(recipes), 6)
        
    def test_get_pizza_margherita_by_mario_batali_recipe(self):
        recipe = tasty.get_recipe('https://tasty.co/recipe/pizza-margherita-by-mario-batali')

        print(recipe.title)
        self.assertEqual(recipe.title, 'Pizza Margherita by Mario Batali')
    
if __name__ == '__main__':
    unittest.main()