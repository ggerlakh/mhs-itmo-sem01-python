import numpy as np
from matrices import Matrix


if __name__ == '__main__':
    np.random.seed(0)
    # Создаем две матрицы
    matrix1 = np.random.randint(0, 10, (10, 10))
    matrix2 = np.random.randint(0, 10, (10, 10))


    A = Matrix(matrix1.tolist())
    B = Matrix(matrix2.tolist())
    with open('artifacts/3.2/matrix+.txt', 'w') as f:
        f.write("Матрица A:\n")
        A.write_to_file(f)
        print("Матрица A:")
        print(A)
        f.write("Матрица B:\n")
        B.write_to_file(f)
        print("Матрица B:")
        print(B)
        f.write("Матрица A+B:\n")
        C = A + B
        C.write_to_file(f)
        print("Матрица A+B:")
        print(C)


    with open('artifacts/3.2/matrix*.txt', 'w') as f:
        f.write("Матрица A:\n")
        A.write_to_file(f)
        print("Матрица A:")
        print(A)
        f.write("Матрица B:\n")
        B.write_to_file(f)
        print("Матрица B:")
        print(B)
        f.write("Матрица A*B:\n")
        C = A * B
        C.write_to_file(f)
        print("Матрица A*B:")
        print(C)

    
    with open('artifacts/3.2/matrix@.txt', 'w') as f:
        f.write("Матрица A:\n")
        A.write_to_file(f)
        print("Матрица A:")
        print(A)
        f.write("Матрица B:\n")
        B.write_to_file(f)
        print("Матрица B:")
        print(B)
        f.write("Матрица A@B:\n")
        C = A @ B
        C.write_to_file(f)
        print("Матрица A@B:")
        print(C)

    
    with open('artifacts/3.2/matrix_t_4.txt', 'w') as f:
        f.write("Матрица A:\n")
        A.write_to_file(f)
        print("Матрица A:")
        print(A)
        T_A = Matrix(A.matrix_data)
        T_A.matrix_data =  A.transpose().tolist()
        f.write("Транспонированная Матрица A:\n")
        T_A.write_to_file(f)
        print("Транспонированная Матрица A:")
        print(T_A)
        A.matrix_data = np.eye(3).tolist()
        f.write("Новая матрица A:\n")
        A.write_to_file(f)
        print("Новая атрица A:")
        print(A)