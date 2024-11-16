import click
import sys
import os


@click.command()
@click.argument('filenames', nargs=-1)
def wc(filenames: tuple):
    counter_dict = {}
    total_lines = None
    """Simple utility displays the number of lines, words, and bytes contained in each input file that works like `wc` command without options."""
    if filenames == ():
        counter_dict["stdin"] = {"lines": 0, "words": 0, "size": 0}
        try:
            while True:
                line = input()
                counter_dict["stdin"]["lines"] += 1
                if line.lstrip(' ') != '' or ' ' in line.lstrip(' '):
                    counter_dict["stdin"]["words"] += len(line.split(' '))
                counter_dict["stdin"]["size"] += len(line.encode('utf-8'))
        except (KeyboardInterrupt, EOFError):
            print(f"      {counter_dict['stdin']['lines']}     {counter_dict['stdin']['words']}    {counter_dict['stdin']['size']}")
    else:
        files_count = len(filenames)
        counter_dict['total'] = {"lines": 0, "words": 0, "size": 0}
        for filename in filenames:
            if os.path.exists(filename):
                counter_dict[filename] = {"lines": 0, "words": 0, "size": os.path.getsize(filename)}
                with open(filename, 'r') as f:
                    for line in f:
                        if line.endswith('\n'):
                            counter_dict[filename]["lines"] += 1
                        line = line.strip('\n')
                        counter_dict[filename]["words"] += len([s for s in line.strip(' ').split(' ') if s != ''])
                counter_dict["total"]["lines"] += counter_dict[filename]["lines"]
                counter_dict["total"]["words"] += counter_dict[filename]["words"]
                counter_dict["total"]["size"] += counter_dict[filename]["size"]
                lines_prefix = " " * (8 - len(str(counter_dict[filename]['lines'])))
                words_prefix = " " * (8 - len(str(counter_dict[filename]['words'])))
                size_prefix = " " * (8 - len(str(counter_dict[filename]['size'])))
                print(f"{lines_prefix}{counter_dict[filename]['lines']}{words_prefix}{counter_dict[filename]['words']}{size_prefix}{counter_dict[filename]['size']} {filename}")
            else:
                print(f"wc: {filename} No such file or directory", file=sys.stderr)
        if files_count > 1:
            total_lines_prefix = " " * (8 - len(str(counter_dict['total']['lines'])))
            total_words_prefix = " " * (8 - len(str(counter_dict['total']['words'])))
            total_size_prefix = " " * (8 - len(str(counter_dict['total']['size'])))
            print(f"{total_lines_prefix}{counter_dict['total']['lines']}{total_words_prefix}{counter_dict['total']['words']}{total_size_prefix}{counter_dict['total']['size']} total")
            total_lines = str(counter_dict['total']['lines'])
           

if __name__ == '__main__':
    wc()