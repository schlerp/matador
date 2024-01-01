import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--host", default="127.0.0.1")
def api():
    from matador.api import app

    app.run()
