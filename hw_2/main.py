from convert_to_tex import generate_table, generate_tex_doc, generate_picture, convert_tex_to_pdf


if __name__ == "__main__":
    path_to_output_tex_file = "./artifacts/table_and_png.tex"
    path_to_png = "./artifacts/python.png"
    with open(path_to_output_tex_file, "w") as tex_file:
        l = [
            ["id", "val", "num", "group"],
            [7, 3, 9, 1],
            [5, True, None, 8],
            ["k", 6, "ABC", 3]
            ]
        tex_file.write(generate_tex_doc(generate_table(l) + generate_picture(path_to_png)))
    convert_tex_to_pdf(path_to_output_tex_file)