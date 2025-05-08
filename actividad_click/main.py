import click
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

@cli.command()
def timenow():
    """Shows the current time"""
    print(f"\n{datetime.now()}\n")
    
@cli.command()
def banner():
    """Shows a banner with the name of UFM"""
    banner = '''
    UUU   UUU  FFFFFF   M     M
    UUU   UUU  F        MM   MM
    UUU   UUU  FFFFF    M M M M
    UUU   UUU  F        M  M  M
    UUUUUUUUU  F        M     M
    '''
    click.echo(banner)

@cli.command()
def favlang():
    """Asks for your favorite programming language and answers in a funny way"""
    language = click.prompt("¿Cuál es tu lenguaje de programación favorito?")
    click.echo(f"Típico escoger {language}, sé más original :/")
        
if __name__ == '__main__':
    cli()
        
        