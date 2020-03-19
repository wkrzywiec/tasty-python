import click
import tasty_python.tasty_client as client

@click.group()
def cli():
    pass

@cli.command()
@click.argument('query', type=click.STRING)
def find(query):
    """Find recipes list that match provided query"""

    results = client.find_reciepes(query)
    if len(results) > 0:
        click.secho("\nThere are following results on the 1. page:", fg='yellow')
        for result in results:
            click.secho("\n\t" + result.full_name, fg='green')
            click.echo("\t\t" + result.key)
            click.echo("\t\t" + result.url + "\n")
    else:
        click.secho("\nThere are no results for a query: " + query, bg='red')
        click.echo("\nBut there are lots of other recipes with chicken, veggies and more...")
        click.echo("So give it another try, maybe next time you'll find the recipe you're looking for.")

@cli.command()
@click.argument('key', type=click.STRING)
@click.option('--url/--key', default=False, help='Indicates if you provide the full link to the recipe')
def get(key, url):
    """Get full recipe by its key"""
    
    if url:
        recipe = client.get_recipe_by_url(key)
    else:
        recipe = client.get_recipe_by_key(key)

    if recipe is not None:
        click.secho('\n\t' + recipe.title, fg='green')
        click.secho('\tSource: ' + recipe.url)
        click.secho('\n\tIngredients:', fg='yellow')
        for section in recipe.ingredients_sections:
            click.secho('\n\t' + section.name)
            for ingredient in section.ingredients:
                click.echo('\t\t' + ingredient)
        click.secho('\n\tPreparation:', fg='yellow')
        for step in recipe.preparation:
            click.echo('\t' + step)
    else:
        if url:
            click.secho("\nProvided url is invalid. Url: {}".format(key), bg='red')
        else:
            click.secho("\nProvided key is invalid. Key: {}".format(key), bg='red')

@cli.command()
@click.argument('key', type=click.STRING)
def launch(key):
    """Launch the recipe in a web brower by its key"""
    click.launch('https://tasty.co/recipe' + key)

if __name__ == '__main__':
    cli()
