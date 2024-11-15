import click
import sys
import os


def get_last_n_lines(filename: str, n: int):
    if n <= 0:
        raise RuntimeError("number of lines must be a positive number")
    with open(filename, 'r') as f:
        stripped_file_lines = [s.rstrip('\n') for s in f.readlines()]
        print('\n'.join(stripped_file_lines[-n:]))


@click.command()
@click.argument('filenames', nargs=-1)
def tail(filenames: tuple):
    """Simple display the last part of a file that works like `tail` command without options."""
    if filenames == ():
        i = 1
        input_lines = []
        try:
            while True:
                s = input()
                input_lines.append(s)
                i += 1
        except (KeyboardInterrupt, EOFError):
            print('\n'.join(input_lines[-17:]))
    else:
        files_count = len(filenames)
        for filename in filenames:
            if os.path.exists(filename):
                if files_count == 1:
                     get_last_n_lines(filename, 17)
                else:
                    print(f"==> {filename} <==")
                    get_last_n_lines(filename, 10)
            else:
                print(f"tail: {filename} No such file or directory", file=sys.stderr)


if __name__ == '__main__':
    tail()