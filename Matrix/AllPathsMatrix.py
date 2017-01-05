
class Solution(object):
    def __init__(self, mat):
        self.mat = mat
        self.r = len(mat)
        self.c = len(mat[0])

    def printAllPaths(self, path, i, j):
        if i == self.r-1 and j == self.c-1:
            path.append(self.mat[i][j])
            print(path)
            return

        path.append(self.mat[i][j])
        # Can go right
        if self.isValid(i+1, j):
            self.printAllPaths(path, i+1, j)
            path.pop()
        # Can go below
        if self.isValid(i, j+1):
            self.printAllPaths(path, i, j+1)
            path.pop()
        # Can go diagonal
        if self.isValid(i+1, j+1):
            self.printAllPaths(path, i+1, j+1)
            path.pop()

    def isValid(self, i, j):
        if i >= self.r or j >= self.c:  # or self.mat[i][j]in [6, 7, 10, 11]:
            return False
        return True

    def printMatrix(self):
        print("######")
        for row in self.mat:
            print(row)
        print("######")


if __name__ == '__main__':
    matrix1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
    ]

    matrix2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]


    s1 = Solution(matrix1)
    s1.printMatrix()
    print("All Possible Paths")
    s1.printAllPaths([], 0, 0)
    s2 = Solution(matrix2)
    s2.printMatrix()
    print("All Possible Paths")
    s2.printAllPaths([], 0, 0)