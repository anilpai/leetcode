class Solution(object):

    def rotateMatrixCounterClockwise(self, mat):
        if len(mat) == 0:
            return

        # To asses the size of N*M matrix
        top = 0
        bottom = len(mat) - 1

        left = 0
        right = len(mat[0]) - 1

        while left < right and top < bottom:

            prev = mat[top][right]

            # Move elements of top row one step left
            for i in range(right-1, left-1, -1):
                curr = mat[top][i]
                mat[top][i] = prev
                prev = curr

            top += 1

            # Move elements of leftmost column one step downwards
            for i in range(top, bottom + 1):
                curr = mat[i][left]
                mat[i][left] = prev
                prev = curr

            left += 1

            # Move elements of bottommost row one stop rightwards
            for i in range(left, right + 1):
                curr = mat[bottom][i]
                mat[bottom][i] = prev
                prev = curr

            bottom -=1

            # Move elements of rightmost column one step upwards
            for i in range(bottom, top-2, -1):
                curr = mat[i][right]
                mat[i][right] = prev
                prev = curr

            right -= 1
        return mat


    def rotateMatrixClockwise(self, mat):
        if not len(mat):
            return

        """
            top : starting row index
            bottom : ending row index
            left : starting column index
            right : ending column index
        """

        top = 0
        bottom = len(mat) - 1

        left = 0
        right = len(mat[0]) - 1

        while left < right and top < bottom:

            prev = mat[top +1][left]

            # Move elements of top row one step right
            for i in range(left, right + 1):
                curr = mat[top][i]
                mat[top][i] = prev
                prev = curr

            top += 1

            # Move elements of rightmost column one step downwards
            for i in range(top, bottom + 1):
                curr = mat[i][right]
                mat[i][right] = prev
                prev = curr

            right -= 1

            # Move elements of bottom row one step left
            for i in range(right, left - 1, -1):
                curr = mat[bottom][i]
                mat[bottom][i] = prev
                prev = curr

            bottom -= 1

            # Move elements of leftmost column one step upwards
            for i in range(bottom, top - 1, -1):
                curr = mat[i][left]
                mat[i][left] = prev
                prev = curr

            left += 1

        return mat


    # Utility Function
    def printMatrix(self, mat):
        print("######")
        for row in mat:
            print(row)
        print("######")


if __name__=='__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    s = Solution()
    s.printMatrix(matrix)
    print("ClockWise Rotation")
    s.printMatrix(s.rotateMatrixClockwise(matrix))
    print("Counter ClockWise Rotation")
    s.printMatrix(s.rotateMatrixCounterClockwise(matrix))