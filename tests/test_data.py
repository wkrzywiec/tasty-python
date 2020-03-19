find_pizza_partial_output = """
\tPizza Margherita by Mario Batali
\t\tpizza-margherita-by-mario-batali
\t\thttps://tasty.co/recipe/pizza-margherita-by-mario-batali"""


find_no_results_output = """\nThere are no results for a query: asdkjh
\nBut there are lots of other recipes with chicken, veggies and more...
So give it another try, maybe next time you'll find the recipe you're looking for.\n"""

get_pizza_margherita_by_mario_batali_recipe = """
\tPizza Margherita by Mario Batali
\tSource: https://tasty.co/recipe/pizza-margherita-by-mario-batali

\tIngredients:

\tDough
\t\t1 ¼ cups water (300 mL), warm
\t\t¼ oz active dry yeast (10 g), 1 packet
\t\t1 ½ teaspoons sugar
\t\t3 ½ cups all-purpose flour (435 g)
\t\t2 tablespoons salt
\t\t¼ cup extra virgin olive oil (60 mL)

\tTopping
\t\t2 cups tomato (400 g), strained
\t\tfresh basil
\t\t8 oz fresh mozzarella cheese (225 g)
\t\tolive oil
\t\tsalt, to taste

\tPreparation:
\t1. In a small mixing bowl, whisk the warm water, yeast, and sugar together. Place in a warm place for 10 minutes, or until yeast is foamy.
\t2. In a large mixing bowl, whisk together the flour and salt.
\t3. Make a well in the center of the dry ingredients and add the yeast mixture and olive oil. Stir the wet ingredients into the dry ingredients until the dough comes together and becomes difficult to stir.
\t4. Turn the dough out onto a lightly floured surface and knead until the dough is smooth, about 5 minutes. Add small amounts of flour as necessary to prevent sticking.
\t5. Transfer the dough to a large bowl coated with olive oil. Cover with a towel and let rise in a warm place for 1-2 hours, until the dough has doubled in size.
\t6. Once the dough has doubled in size, remove the towel and punch the dough down. Turn out onto a lightly floured surface and divide the dough into 6-8 pieces, and shape each into a small ball.
\t7. Place the formed balls onto a baking sheet and rest, covered, for 15 minutes.
\t8. To shape the individual pizzas, press out the dough balls onto a lightly floured surface. Create a slightly thicker rim around the outside of the dough and continue to stretch into a 9- to 10-inch (23-25 cm) round.
\t9. Heat a large cast-iron pan over medium heat, until the pan just begins to smoke, about 5 minutes.
\t10. Carefully transfer a stretched pizza round onto the hot pan. Leave to cook for 2-3 minutes (the dough should begin bubbling up) until lightly tanned with a few dark spots. Flip and continue to cook on the other side for 1-2 minutes longer, until the crust is completely dry.
\t11. Remove the dough to rest on a wire rack and repeat with remaining dough.
\t12. To finish the pizzas, top each crust with tomato sauce and fresh mozzarella.
\t13. Transfer to the oven and broil for 7 or 8 minutes, until the cheese has melted and the crust has developed a nice char in spots. Watch closely and move to a lower rack if necessary.
\t14. Finish each pizza with fresh basil, a drizzle of olive oil, and a sprinkle of salt.
\t15. Enjoy!
"""
get_invalid_recipe_key_output = """\nProvided key is invalid. Key: {}\n"""

get_invalid_recipe_url_output = """\nProvided url is invalid. Url: {}\n"""