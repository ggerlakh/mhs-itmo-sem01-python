import click
import os


@click.command()
@click.argument('filename', default="")
def nl(filename):
    """Simple line numbering filter that works like `nl -b a`"""
    if filename == "":
        i = 1
        while True:
            s = input()
            curr_idx_len = len(str(i))
            space_prefix = " " * (5 - curr_idx_len + 1)
            print(f"{space_prefix}{i}  {s}")
            i += 1
    else:
        if os.path.exists(filename):
            # print(f"successfully found filename = {filename}")
            with open(filename, 'r') as f:
                i = 1
                curr_idx_len = 1
                for line in f:
                    curr_idx_len = len(str(i))
                    space_prefix = " " * (5 - curr_idx_len + 1)
                    stripped_line = line.rstrip('\n')
                    print(f"{space_prefix}{i}  {stripped_line}")
                    i += 1
        else:
            print(f"nl: {filename} No such file or directory")


if __name__ == '__main__':
    nl()