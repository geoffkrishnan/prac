import click

from .database import init_db, add_problem, list_problems
from supermemo2 import sm_two, first_review, review, timedelta, datetime


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
