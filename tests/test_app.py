import tasty_python.cli as app
import unittest
from click.testing import CliRunner
import tests.test_data as test_data

class TestCliApp(unittest.TestCase):
    runner = CliRunner()

    def test_find_recipe(self):
        result = self.runner.invoke(app.find, ['pizza'])
  
        expected_result = test_data.find_pizza_partial_output
        self.assertIn(expected_result, result.output)

    def test_find_no_recipe(self):
        result = self.runner.invoke(app.find, ['asdkjh'])

        expected_result = test_data.find_no_results_output
        self.assertIn(expected_result, result.output)

    
    def test_get_recipe_by_key(self):
        result = self.runner.invoke(app.get, ['pizza-margherita-by-mario-batali'])

        expected_result = test_data.get_pizza_margherita_by_mario_batali_recipe
        self.assertEqual(expected_result, result.output)

    def test_get_recipe_by_url(self):
        result = self.runner.invoke(app.get, ['https://tasty.co/recipe/pizza-margherita-by-mario-batali', '--url'])

        expected_result = test_data.get_pizza_margherita_by_mario_batali_recipe
        self.assertEqual(expected_result, result.output)

    def test_get_recipe_by_invalid_key(self):
        key = 'sdnwknlk'
        result = self.runner.invoke(app.get, [key])

        expected_result = test_data.get_invalid_recipe_key_output.format(key)
        self.assertEqual(expected_result, result.output)

    def test_get_recipe_by_invalid_url(self):
        url = 'https://tasty.co/recipe/dsfd'
        result = self.runner.invoke(app.get, [url, '--url'])

        expected_result = test_data.get_invalid_recipe_url_output.format(url)
        self.assertEqual(expected_result, result.output)
    

if __name__ == '__main__':
    unittest.main()
