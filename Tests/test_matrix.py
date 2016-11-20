from unittest import TestCase
from Matrix.MatrixInSpiral import Solution as a
from Matrix.MatrixRotate90deg import Solution as b
from Matrix.RotateMatrix import Solution as c


class TestSolution(TestCase):
    def test_spiralmatrix(self):
        r = a()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertListEqual(r.SpiralMatrix(matrix), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],'Spiral Matrix')

    def test_matrixRotate(self):
        r = b()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertListEqual(r.Rotate90Clock(matrix), [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]], 'Rotate 90 clockwise')
        self.assertListEqual(r.Rotate90CounterClock(matrix), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 'Rotate 90 anti-clockwise')

    def test_matrixMove(self):
        r = c()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertListEqual(r.rotateMatrixClockwise(matrix), [[5, 1, 2, 3], [9, 10, 6, 4], [13, 11, 7, 8], [14, 15, 16, 12]], 'Rotate one step clockwise')
        self.assertListEqual(r.rotateMatrixCounterClockwise(matrix), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 'Rotate one step anti-clockwise')