import click
import sys


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def tail(files):
    if files:
        for file_name in files:
            if len(files) > 1:
                click.echo(f'==> {file_name} <==')
            with open(file_name, 'r') as file:
                lines = file.readlines()
                last_lines = lines[-10:]
                for line in last_lines:
                    click.echo(line, nl=False)
            click.echo('\n', nl=True)
    else:
        lines = sys.stdin.readlines()
        last_lines = lines[-17:]
        for line in last_lines:
            click.echo(line, nl=False)


if __name__ == "__main__":
    tail()
