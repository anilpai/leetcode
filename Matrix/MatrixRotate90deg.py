# An Inplace function to rotate a N x N matrix by 90 degrees
# In both clockwise and counter clockwise direction


class Solution(object):
    def Rotate90Clock(self, mat):

        N = len(mat)
        for x in range(int(N/2)):
            for y in range(x, N-x-1):
                temp = mat[x][y]

                '''
                Move values from left to top.
                Move values from bottom to left.
                Move values from right to bottom.
                Move values from top to right.
                '''

                mat[x][y] = mat[N-1-y][x]
                mat[N-1-y][x] = mat[N-1-x][N-1-y]
                mat[N-1-x][N-1-y] = mat[y][N-1-x]
                mat[y][N-1-x] = temp
        return mat

    def Rotate90CounterClock(self, mat):

        N = len(mat)

        for x in range(0, int(N/2)):
            for y in range(x, N-x-1):
                temp = mat[x][y]

                '''
                Move values from right to top.
                Move values from bottom to right.
                Move values from left to bottom.
                Move values from left to bottom.
                '''

                mat[x][y] = mat[y][N-1-x]
                mat[y][N-1-x] = mat[N-1-x][N-1-y]
                mat[N-1-x][N-1-y] = mat[N-1-y][x]
                mat[N-1-y][x] = temp
        return mat

    def printMatrix(self, mat):
        # Utility Function
        print("######")
        for row in mat:
            print(row)

if __name__=='__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(matrix)
    s.printMatrix(matrix)
    s.printMatrix(s.Rotate90Clock(matrix))
    s.printMatrix(s.Rotate90CounterClock(matrix))