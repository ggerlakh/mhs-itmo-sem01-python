from typing import List


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
    return "\\documentclass{article}\n" + "\\usepackage{graphicx}\n" + "\\begin{document}\n" + tex_table_str + "\end{document}\n"