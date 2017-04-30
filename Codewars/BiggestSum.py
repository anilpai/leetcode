'''
Biggest Sum from Top left to Bottom Right
'''


def find_sum(m):
    p = [0] * (len(m) + 1)
    for l in m:
        for i, v in enumerate(l, 1):
            p[i] = v + max(p[i-1], p[i])
    return p[-1]


matrix = [[20, 20, 10, 10],
          [10, 20, 10, 10],
          [10, 20, 20, 20],
          [10, 10, 10, 20]]

print(find_sum(matrix) == 140)
