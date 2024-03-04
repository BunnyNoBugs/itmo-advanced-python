import click
import sys


def count_statistics(file):
    lines = 0
    words = 0
    bytes_count = 0

    for line in file:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode('utf-8'))

    return lines, words, bytes_count


@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
def wc(files):
    total_lines = 0
    total_words = 0
    total_bytes = 0

    if not files:
        lines, words, bytes_count = count_statistics(sys.stdin)
        click.echo(f'{lines}\t{words}\t{bytes_count}')
        return

    for file in files:
        lines, words, bytes_count = count_statistics(file)
        total_lines += lines
        total_words += words
        total_bytes += bytes_count
        click.echo(f'{lines}\t{words}\t{bytes_count}\t{file.name}')

    if len(files) > 1:
        click.echo(f'{total_lines}\t{total_words}\t{total_bytes}\ttotal')


if __name__ == "__main__":
    wc()
