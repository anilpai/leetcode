
class Solution(object):
    def SpiralMatrix(self, mat):
        '''
        Clockwise Rotation
        '''

        l =[]

        top = 0
        bottom = len(mat)-1

        left= 0
        right = len(mat[0])-1

        while left < right and top < bottom:

            for i in range(left,right+1):
                l.append(mat[top][i])

            top += 1

            for i in range(top, bottom+1):
                l.append(mat[i][right])

            right -= 1

            for i in range(right, left-1, -1):
                l.append(mat[bottom][i])

            bottom -= 1

            for i in range(bottom, top-1, -1):
                l.append(mat[i][left])

            left +=1

        return l

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
    print("Spiral Matrix")
    print(s.SpiralMatrix(matrix))

    # matrix = [
    #     [1, 2, 3, 4, 5, 6],
    #     [7, 8, 9, 10, 11, 12],
    #     [13, 14, 15, 16, 17, 18]
    # ]
    # s.printMatrix(matrix)
    # print("Spiral Matrix")
    # print(s.SpiralMatrix(matrix))