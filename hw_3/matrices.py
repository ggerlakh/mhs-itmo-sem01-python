import numpy as np


class MatrixNumpy(np.ndarray):
    def __new__(cls, data):
        if not isinstance(data, (list)):
            raise TypeError("Matrix data must be a list")
        obj = np.asarray(data).view(cls)
        return obj

class MatrixStrOutput:
    def __str__(self):
        res_str = ""
        for i in range(self.n):
            res_str += (' '.join(list(map(str, self._matrix_data[i]))) + "\n")
        return res_str
    
"""
Простая хеш-функция, сумма диагональных элементов матрицы
Коллизия если mat1.trace() == mat2.trace() при разных элеменах матрицы, пример
[
[-1, 4],
[5, 1]
]

[
[5, 33],
[9, -5]
]
"""
class MatrixHash:
    def __hash__(self):
        return int(self.trace())


class MatrixFileOutput:
    def write_to_file(self, fp):
        fp.write(str(self))


class MatrixDescriptor:

    @property
    def matrix_data(self):
        return self._matrix_data
    
    @matrix_data.setter
    def matrix_data(self, data):
        if not isinstance(data, list):
            raise TypeError("Matrix data must be a list")
        self._matrix_data = data
        self.n = len(data)
        self.m = len(data[0])


class Matrix(MatrixHash, MatrixFileOutput, MatrixDescriptor, MatrixStrOutput, MatrixNumpy):

    def __init__(self, data):
        self._matrix_data = data
        self.n = len(data)
        self.m = len(data[0])

    def __add__(self, other):
        if other.n != self.n or other.m != self.m:
            raise ValueError("Error! Wrong matrices sizes for sum")
        res_data = []
        for i in range(self.n):
            res_data.append([0 for _ in range(self.m)])
        for i in range(self.n):
            for j in range(self.m):
                res_data[i][j] = (self._matrix_data[i][j] + other._matrix_data[i][j])
        return self.__class__(res_data)

    def __mul__(self, other):
        if other.n != self.n or other.m != self.m:
            raise ValueError("Error! Wrong matrices sizes for sum")
        res_data = []
        for i in range(self.n):
            res_data.append([0 for _ in range(self.m)])
        for i in range(self.n):
            for j in range(self.m):
                res_data[i][j] = (self._matrix_data[i][j] * other._matrix_data[i][j])
        return self.__class__(res_data)

    def __matmul__(self, other):
        if self.n != other.m:
            raise ValueError("Error! Wrong matrices sizes for multiplication")
        res_data = []
        for i in range(self.n):
            res_data.append([0 for _ in range(other.m)])
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    res_data[i][j] += (self._matrix_data[i][k] * other._matrix_data[k][j])
        return self.__class__(res_data)
