import unittest
import tasty_python.tasty_client as tasty

class TestTastyClient(unittest.TestCase):

    def test_find_pizza_margherita_recipes(self):
        recipes = tasty.find_reciepes('pizza margherita')
        self.assertGreaterEqual(len(recipes), 6)

    def test_find_no_results(self):
        recipes = tasty.find_reciepes('dsfkjsdh')
        self.assertEqual(len(recipes), 0)

    def test_find_empty_query(self):
        recipes = tasty.find_reciepes('')
        self.assertEqual(len(recipes), 0)

    def test_get_pizza_margherita_by_mario_batali_recipe(self):
        recipe = tasty.get_recipe_by_url('https://tasty.co/recipe/pizza-margherita-by-mario-batali')

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

        preparation_steps = recipe.preparation
        self.assertEqual(len(preparation_steps), 15)
        self.assertEqual(preparation_steps[0], '1. In a small mixing bowl, whisk the warm water, yeast, and sugar together. Place in a warm place for 10 minutes, or until yeast is foamy.')
        self.assertEqual(preparation_steps[1], '2. In a large mixing bowl, whisk together the flour and salt.')
        self.assertEqual(preparation_steps[2], '3. Make a well in the center of the dry ingredients and add the yeast mixture and olive oil. Stir the wet ingredients into the dry ingredients until the dough comes together and becomes difficult to stir.')
        self.assertEqual(preparation_steps[3], '4. Turn the dough out onto a lightly floured surface and knead until the dough is smooth, about 5 minutes. Add small amounts of flour as necessary to prevent sticking.')
        self.assertEqual(preparation_steps[4], '5. Transfer the dough to a large bowl coated with olive oil. Cover with a towel and let rise in a warm place for 1-2 hours, until the dough has doubled in size.')
        self.assertEqual(preparation_steps[5], '6. Once the dough has doubled in size, remove the towel and punch the dough down. Turn out onto a lightly floured surface and divide the dough into 6-8 pieces, and shape each into a small ball.')
        self.assertEqual(preparation_steps[6], '7. Place the formed balls onto a baking sheet and rest, covered, for 15 minutes.')
        self.assertEqual(preparation_steps[7], '8. To shape the individual pizzas, press out the dough balls onto a lightly floured surface. Create a slightly thicker rim around the outside of the dough and continue to stretch into a 9- to 10-inch (23-25 cm) round.')
        self.assertEqual(preparation_steps[8], '9. Heat a large cast-iron pan over medium heat, until the pan just begins to smoke, about 5 minutes.')
        self.assertEqual(preparation_steps[9], '10. Carefully transfer a stretched pizza round onto the hot pan. Leave to cook for 2-3 minutes (the dough should begin bubbling up) until lightly tanned with a few dark spots. Flip and continue to cook on the other side for 1-2 minutes longer, until the crust is completely dry.')
        self.assertEqual(preparation_steps[10], '11. Remove the dough to rest on a wire rack and repeat with remaining dough.')
        self.assertEqual(preparation_steps[11], '12. To finish the pizzas, top each crust with tomato sauce and fresh mozzarella.')
        self.assertEqual(preparation_steps[12], '13. Transfer to the oven and broil for 7 or 8 minutes, until the cheese has melted and the crust has developed a nice char in spots. Watch closely and move to a lower rack if necessary.')
        self.assertEqual(preparation_steps[13], '14. Finish each pizza with fresh basil, a drizzle of olive oil, and a sprinkle of salt.')
        self.assertEqual(preparation_steps[14], '15. Enjoy!')
    
    def test_get_recipe_by_invalid_key(self):
        recipe = tasty.get_recipe_by_key('asdjksdjh')
        self.assertIsNone(recipe)

    def test_get_recipe_by_invalid_url(self):
        recipe = tasty.get_recipe_by_url('https://tasty.co/recipe/asdjksdjh')
        self.assertIsNone(recipe)


if __name__ == '__main__':
    unittest.main()