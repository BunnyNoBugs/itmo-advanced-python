import click
import sys


@click.command()
@click.argument('input_file', type=click.File('r'), required=False)
def nl(input_file):
    if input_file:
        lines = input_file.readlines()
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines, start=1):
        click.echo(f'{i}\t{line}', nl=False)


if __name__ == '__main__':
    nl()
