

class Matrix:

    def __init__(self, data):
        self.data = data
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
                res_data[i][j] = (self.data[i][j] + other.data[i][j])
        return self.__class__(res_data)

    def __mul__(self, other):
        if other.n != self.n or other.m != self.m:
            raise ValueError("Error! Wrong matrices sizes for sum")
        res_data = []
        for i in range(self.n):
            res_data.append([0 for _ in range(self.m)])
        for i in range(self.n):
            for j in range(self.m):
                res_data[i][j] = (self.data[i][j] * other.data[i][j])
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
                    res_data[i][j] += (self.data[i][k] * other.data[k][j])
        return self.__class__(res_data)
        