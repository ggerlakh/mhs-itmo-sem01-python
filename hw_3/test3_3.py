import numpy as np
from matrices import Matrix


if __name__ == '__main__':
    A = Matrix([
        [-1, 4],
        [5, 1]
    ])
    B = Matrix([
        [5, 33],
        [9, -5]
    ])
    C = Matrix([
        [1, 0],
        [0, 1]
    ])
    D = Matrix([
        [1, 0],
        [0, 1]
    ])
    with open('artifacts/3.3/A.txt', 'w') as f:
        f.write("Матрица A:\n")
        A.write_to_file(f)
        print("Матрица A:")
        print(A)


    with open('artifacts/3.3/B.txt', 'w') as f:
        f.write("Матрица B:\n")
        B.write_to_file(f)
        print("Матрица B:")
        print(B)


    with open('artifacts/3.3/C.txt', 'w') as f:
        f.write("Матрица C:\n")
        C.write_to_file(f)
        print("Матрица C:")
        print(C)

    with open('artifacts/3.3/D.txt', 'w') as f:
        f.write("Матрица D:\n")
        D.write_to_file(f)
        print("Матрица D:")
        print(D)

    
    with open('artifacts/3.3/AB.txt', 'w') as f:
        f.write("Матрица A:\n")
        A.write_to_file(f)
        print("Матрица A:")
        print(A)
        f.write("Матрица B:\n")
        B.write_to_file(f)
        print("Матрица B:")
        print(B)
        f.write("Матрица A@B:\n")
        mul_a_b = A @ B
        mul_a_b.write_to_file(f)
        print("Матрица A@B:")
        print(mul_a_b)

    
    with open('artifacts/3.3/CD.txt', 'w') as f:
        f.write("Матрица C:\n")
        C.write_to_file(f)
        print("Матрица C:")
        print(C)
        f.write("Матрица D:\n")
        D.write_to_file(f)
        print("Матрица D:")
        print(D)
        f.write("Матрица C@D:\n")
        mul_c_d = C @ D
        mul_c_d.write_to_file(f)
        print("Матрица C@D:")
        print(mul_c_d)
    

    with open('artifacts/3.3/hash.txt', 'w') as f:
        f.write(f"hash(A@B) = {hash(mul_a_b)}\n")
        print(f"hash(A@B) = {hash(mul_a_b)}")
        f.write(f"hash(C@D) = {hash(mul_c_d)}\n")
        print(f"hash(C@D) = {hash(mul_c_d)}")