import tasty_python.app as app
import unittest
from click.testing import CliRunner

class TestCliApp(unittest.TestCase):

    def test_find_recipe(self):
        runner = CliRunner()
        result = runner.invoke(app.find, ['pizza'])
  
        expected_result = """
\tPizza Margherita by Mario Batali
\t\tpizza-margherita-by-mario-batali
\t\thttps://tasty.co/recipe/pizza-margherita-by-mario-batali"""

        self.assertIn(expected_result, result.output)

    def test_find_no_recipe(self):
        runner = CliRunner()
        result = runner.invoke(app.find, ['asdkjh'])

        expected_result = """\nThere are no results for a query: asdkjh
\nBut there are lots of other recipes with chicken, veggies and more...
So give it another try, maybe next time you'll find the recipe you're looking for.\n"""

        self.assertIn(expected_result, result.output)

    

if __name__ == '__main__':
    unittest.main()