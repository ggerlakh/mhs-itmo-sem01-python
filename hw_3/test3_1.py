import numpy as np
from matrices import Matrix


if __name__ == '__main__':
    np.random.seed(0)
    # Создаем две матрицы
    matrix1 = np.random.randint(0, 10, (10, 10))
    matrix2 = np.random.randint(0, 10, (10, 10))

    # Выводим матрицы на экран
    print("Первая матрица:\n", matrix1)
    print("\nВторая матрица:\n", matrix2)


    A = Matrix(matrix1.tolist())
    B = Matrix(matrix2.tolist())
    with open('artifacts/3.1/matrix+.txt', 'w') as f:
        f.write("Матрица A:\n")
        f.write(str(A.data).replace('],', '],\n')+"\n")
        f.write("Матрица B:\n")
        f.write(str(B.data).replace('],', '],\n')+"\n")
        f.write("Матрица A+B:\n")
        C = A + B
        print("Матрица A+B:\n"+str(C.data).replace('],', '],\n')+"\n")
        f.write(str(C.data).replace('],', '],\n')+"\n")

    
    with open('artifacts/3.1/matrix*.txt', 'w') as f:
        f.write("Матрица A:\n")
        f.write(str(A.data).replace('],', '],\n')+"\n")
        f.write("Матрица B:\n")
        f.write(str(B.data).replace('],', '],\n')+"\n")
        f.write("Матрица A*B:\n")
        C = A * B
        print("Матрица A*B:\n"+str(C.data).replace('],', '],\n')+"\n")
        f.write(str(C.data).replace('],', '],\n')+"\n")

    
    with open('artifacts/3.1/matrix@.txt', 'w') as f:
        f.write("Матрица A:\n")
        f.write(str(A.data).replace('],', '],\n')+"\n")
        f.write("Матрица B:\n")
        f.write(str(B.data).replace('],', '],\n')+"\n")
        f.write("Матрица A@B:\n")
        C = A @ B
        print("Матрица A@B:\n"+str(C.data).replace('],', '],\n')+"\n")
        f.write(str(C.data).replace('],', '],\n')+"\n")
        print("np A@B:")
        print(matrix1@matrix2)