import os
import pathlib
import subprocess
from typing import List


def generate_tex_doc(tex_content: str) -> str:
    return "\\documentclass{article}\n" + "\\usepackage{graphicx}\n" + "\\begin{document}\n" + tex_content + "\end{document}\n"


def generate_table(inp_list: List[List[any]]) -> str:
    tex_table_cells_alignment = "|"
    for i in range(len(inp_list[0])):
        tex_table_cells_alignment += "c|"
    tex_table_str = "\\begin{tabular}{" + tex_table_cells_alignment + "}\n"
    tex_table_str += "\\hline\n"
    for row in inp_list:
        tex_table_row = ' & '.join(list(map(str, row))) + "\\\\\n"
        tex_table_row += "\\hline\n"
        tex_table_str += tex_table_row
    tex_table_str += "\\end{tabular}\n"
    return tex_table_str


def generate_picture(pic_png_path: str) -> str:
    dirname = str(pathlib.Path(pic_png_path).parent.resolve())
    filename = pathlib.Path(pic_png_path).stem
    return "\\graphicspath{ {" + dirname + "} }\n" + "\n\\includegraphics{" + filename + "}\n"


def convert_tex_to_pdf(path_to_tex: str) -> None:
    dirname = str(pathlib.Path(path_to_tex).parent.resolve())
    proc = subprocess.run(f"pdflatex -output-directory={dirname} {path_to_tex}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    proc.check_returncode()
    os.remove(path_to_tex[:-4] + ".log")
    os.remove(path_to_tex[:-4] + ".aux")