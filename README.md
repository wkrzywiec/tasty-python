# Tasty Python
![Python Master Workflow](https://github.com/wkrzywiec/tasty-python/workflows/Python%20Master%20Workflow/badge.svg) [![CodeFactor](https://www.codefactor.io/repository/github/wkrzywiec/tasty-python/badge)](https://www.codefactor.io/repository/github/wkrzywiec/tasty-python) [![codecov](https://codecov.io/gh/wkrzywiec/tasty-python/branch/master/graph/badge.svg)](https://codecov.io/gh/wkrzywiec/tasty-python) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

**Tasty Python** application is a command line tool (CLI) which helps you find and get recipes from a popular cooking website - *https://tasty.co*.

## Usage

*Tasty Python* supports 3 command line methods:

```
$ pipenv run app.py --help
Usage: app.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  find    Find recipes list that match provided query Arguments: query...
  get     Get full recipe by its key Arguments: key {string} -- key or url...
  launch  Launch the recipe in a web brower by its key Arguments: key...
```

#### `find` method
```
$ pipenv run app.py find --help
Usage: app.py find [OPTIONS] QUERY

  Find recipes list that match provided query

  Arguments:     query {string} -- search query

Options:
  --help  Show this message and exit.
```

Example usage:
```
$ pipenv run app.py find pizza

There are following results on the 1. page:

        Pizza Margherita by Mario Batali
                pizza-margherita-by-mario-batali
                https://tasty.co/recipe/pizza-margherita-by-mario-batali


        15-Minute Garlic Bread Pizza
                15-minute-garlic-bread-pizza
                https://tasty.co/recipe/15-minute-garlic-bread-pizza


        Pizza Sticks 3-Ways
                pizza-sticks-3-ways
                https://tasty.co/recipe/pizza-sticks-3-ways

```

#### `get` method
```
$ pipenv run app.py get --help
Usage: app.py get [OPTIONS] KEY

  Get full recipe by its key

  Arguments:     key {string} -- key or url of a recipe     url {boolean} --
  indicates if first argument is a recipe key or its url

Options:
  --url / --key  Indicates if you provide the full link to the recipe
  --help         Show this message and exit.
```

Example usages:
* get recipe by its key
```
$ pipenv run app.py get pizza-margherita-by-mario-batali

Pizza Margherita by Mario Batali
        Source: https://tasty.co/recipe/pizza-margherita-by-mario-batali

        Ingredients:

        Dough
                1 ¼ cups water (300 mL), warm
                ¼ oz active dry yeast (10 g), 1 packet
                1 ½ teaspoons sugar
                3 ½ cups all-purpose flour (435 g)
                2 tablespoons salt
                ¼ cup extra virgin olive oil (60 mL)

        Topping
                2 cups tomato (400 g), strained
                fresh basil
                8 oz fresh mozzarella cheese (225 g)
                olive oil
                salt, to taste

        Preparation:
        1. In a small mixing bowl, whisk the warm water, yeast, and sugar together. Place in a warm place for 10 minutes, or until yeast is foamy.     
        2. In a large mixing bowl, whisk together the flour and salt.
        3. Make a well in the center of the dry ingredients and add the yeast mixture and olive oil. Stir the wet ingredients into the dry ingredients 
until the dough comes together and becomes difficult to stir.
        4. Turn the dough out onto a lightly floured surface and knead until the dough is smooth, about 5 minutes. Add small amounts of flour as necessary to prevent sticking.
        5. Transfer the dough to a large bowl coated with olive oil. Cover with a towel and let rise in a warm place for 1-2 hours, until the dough has doubled in size.
        6. Once the dough has doubled in size, remove the towel and punch the dough down. Turn out onto a lightly floured surface and divide the dough 
into 6-8 pieces, and shape each into a small ball.
        7. Place the formed balls onto a baking sheet and rest, covered, for 15 minutes.
        8. To shape the individual pizzas, press out the dough balls onto a lightly floured surface. Create a slightly thicker rim around the outside of the dough and continue to stretch into a 9- to 10-inch (23-25 cm) round.
        9. Heat a large cast-iron pan over medium heat, until the pan just begins to smoke, about 5 minutes.
        10. Carefully transfer a stretched pizza round onto the hot pan. Leave to cook for 2-3 minutes (the dough should begin bubbling up) until lightly tanned with a few dark spots. Flip and continue to cook on the other side for 1-2 minutes longer, until the crust is completely dry.
        11. Remove the dough to rest on a wire rack and repeat with remaining dough.
        12. To finish the pizzas, top each crust with tomato sauce and fresh mozzarella.
        13. Transfer to the oven and broil for 7 or 8 minutes, until the cheese has melted and the crust has developed a nice char in spots. Watch closely and move to a lower rack if necessary.
        14. Finish each pizza with fresh basil, a drizzle of olive oil, and a sprinkle of salt.
        15. Enjoy!
```

* get recipe by its url
```
$ pipenv run app.py get https://tasty.co/recipe/pizza-margherita-by-mario-batali --url

Same result as above

```

#### `launch` method
```
$ pipenv run app.py launch --help
Usage: app.py launch [OPTIONS] KEY

  Launch the recipe in a web brower by its key

  Arguments:     key {string} -- key of a recipe

Options:
  --help  Show this message and exit.
```

## Prerequsites

In order to run tha application you need to have installed:
* Python v3.8
* Pipenv version 2018.11.26