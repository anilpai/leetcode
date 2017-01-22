'''
Largest Palindrome of two N-digit numbers given
N = 1, 2, 3, 4
'''


def largePali4digit():
    answer = 0
    for i in range(9999, 1000, -1):
        for j in range(i, 1000, -1):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > answer:
                return i, j


def largePali3digit():
    answer = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > answer:
                return i, j


def largePali2digit():
    answer = 0
    for i in range(99, 10, -1):
        for j in range(i, 10, -1):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > answer:
                return i, j


def largePali1digit():
    answer = 0
    for i in range(9, 1, -1):
        for j in range(i, 1, -1):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > answer:
                return i, j


print(largePali3digit())
print(largePali2digit())
print(largePali1digit())
print(largePali4digit())