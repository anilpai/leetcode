# w = [1, 2, 4, 2, 5]
# v = [5, 3, 5, 3, 2]
# C = 10

'''
'w' is the weights of items.
'v' is the values of items.
'''

w = [1, 3, 4, 5]
v = [1, 4, 5, 7]

# Naive version.

print("### Naive solution. ###")


def KS(n, C):
    if n==0 or C==0:
        res = 0
    elif w[n] > C:
        res = KS(n-1, C)
    else:
        tmp1 = KS(n-1,C)
        tmp2 = v[n] + KS(n-1, C-w[n])
        res = max(tmp1, tmp2)
    return res


C = 7
print(KS(len(w)-1, C))


'''
Dynamic Programming based solution.
Source: GeeksforGeeks.com
'''

print("### Dynamic Programming based solution. ###")


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))