import click

from .database import (
    init_db,
    add_problem,
    list_problems,
    review_problems,
    complete_problem,
    bulk_add_problems,
)


@click.group()
def cli():
    init_db()


@cli.command()
@click.argument("url")
@click.argument("problem_number", type=int)
@click.argument("name", required=False, default=None)
def add(url, problem_number, name):
    add_problem(url, name, problem_number)


@cli.command()
def list():
    list_problems()


@cli.command()
def review():
    review_problems()


@cli.command()
@click.argument("problem_number", type=int)
@click.argument("quality", type=int)
def complete(problem_number, quality):
    complete_problem(problem_number, quality)


@cli.command()
@click.argument("filepath")
def bulk_add(filepath):
    bulk_add_problems(filepath)
