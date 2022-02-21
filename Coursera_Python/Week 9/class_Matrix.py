import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, m):
        self.mat = copy.deepcopy(m)

    def __str__(self):
        a = ''
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                if j != len(self.mat[i]) - 1:
                    a += str(self.mat[i][j]) + '\t'
                else:
                    a += str(self.mat[i][j])
            if i != len(self.mat) - 1:
                a += '\n'
        return a

    def __add__(self, other):
        if len(self.mat) == len(other.mat) and \
                len(self.mat[0]) == len(other.mat[0]):
            return Matrix([[self.mat[i][j] + other.mat[i][j]
                            for j in range(len(self.mat[0]))]
                           for i in range(len(self.mat))])
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            z = [[0] * len(self.mat) for i in range(len(self.mat[0]))]
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    z[i][j] = self.mat[i][j] * other
            return Matrix(z)
        if isinstance(other, Matrix):
            if len(self.mat[0]) == len(other.mat):
                res = []
                for z in range(len(self.mat)):
                    stroka = []
                    for i in range(len(other.mat[0])):
                        sum = 0
                        for j in range(len(self.mat[0])):
                            p = self.mat[z][j] * other.mat[j][i]
                            sum += p
                        stroka.append(sum)
                    res.append(stroka)
                return Matrix(res)
            else:
                raise MatrixError(self, other)

    __rmul__ = __mul__

    def size(self):
        return len(self.mat), len(self.mat[0])

    def transpose(self):
        self.mat = [[self.mat[i][j] for i in range(len(self.mat))]
                    for j in range(len(self.mat[0]))]
        return Matrix(self.mat)

    @staticmethod
    def transposed(other):
        return Matrix([[other.mat[i][j] for i in range(len(other.mat))]
                       for j in range(len(other.mat[0]))])


a = Matrix([[1, 2], [1, 3]])
print(a)
