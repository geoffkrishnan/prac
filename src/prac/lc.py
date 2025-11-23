import click

from database import init_db, add_problem, list_problems


@click.group()
def cli():
    init_db()


@cli.command()
@click.argument("url")
def add(url):
    add_problem(url)


@cli.command()
def list():
    list_problems()
