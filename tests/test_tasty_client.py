import unittest
import tasty_python.tasty as tasty

class TestTastyClient(unittest.TestCase):

    def test_find_pizza_margherita_recipes(self):
        recipes = tasty.find_reciepes('pizza margherita')
        self.assertGreaterEqual(len(recipes), 6)
        
        for recipe in recipes:
            print(recipe.key)
            print(recipe.full_name)
            print(recipe.url)
            print()
    
if __name__ == '__main__':
    unittest.main()