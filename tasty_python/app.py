import click
import tasty_client as client


@click.group()
def cli():
    pass

@cli.command()
@click.argument('query', type=click.STRING)
def find(query):
    """Find recipes list that match provided query"""

    results = client.find_reciepes(query)
    if len(results > 0):
        click.secho("\nThere are following results on the 1. page:", fg='yellow')
        for result in results:
            click.secho("\n\t" + result.full_name, fg='green', underline=True)
            click.echo("\t\t" + result.key)
            click.echo("\t\t" + result.url + "\n")
    else:
        click.secho("\nThere are no results for a query: " + query, bg='red')

@cli.command()
def get():
    """Get full recipe"""
    click.echo('get')

@cli.command()
def launch():
    """Launch the recipe in a web brower"""


if __name__ == '__main__':
    cli()