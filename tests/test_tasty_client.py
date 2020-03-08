import unittest
import tasty_python.tasty as tasty

class TestTastyClient(unittest.TestCase):

    def test_find_pizza_margherita_recipes(self):
        recipes = tasty.find_reciepes('pizza margherita')
        
        self.assertGreaterEqual(len(recipes), 6)
    
if __name__ == '__main__':
    unittest.main()