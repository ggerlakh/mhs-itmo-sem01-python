from convert_to_tex import generate_table


if __name__ == "__main__":
    path_to_tex_file = "./artifacts/table.tex"
    with open(path_to_tex_file, "w") as tex_file:
        l = [
            ["id", "val", "num", "group"],
            [7, 3, 9, 1],
            [5, True, None, 8],
            ["k", 6, "ABC", 3]
            ]
        tex_file.write(generate_table(l))