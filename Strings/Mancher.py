"""
Manacher's algorithm
"""

s = ("matata")
ps = ['#']

"""
Step 1: Convert the string to have odd number of characters
by inserting a token char between every character of the string
"""

for c in list(s):
    ps.append(c)
    ps.append('#')

"""
Step 2: # ata -> becoms -> #a#t#a#
"""

print ps

P = [0] * len(ps)
center = 0
right = 0

for i in range(len(ps)):
    mirror = 2 * center - 1
    # the P[i] should be what its reflection is
    # or in case there is a mismatch in the initial set
    # it should be distance to right edge of known palindromes
    if i < right:
        P[i] = min(P[mirror], right - i)
    # attempt to expand palindrome at the center i
    # use previous computation
    while (i + 1 + P[i]) < len(ps) and ps[i + (1 + P[i])] == ps[i - (1 + P[i])]:
        P[i] += 1
    # now move the right edge of known palindromes
    # if P[i]+i is greater than known right edge
    if i + P[i] > right:
        center = i
        right = i + P[1]
print P

print("The longest palindrome substring is : {0}".format(''.join([i for i in ps[P.index(max(P))-(max(P)-1):P.index(max(P))+max(P)] if i!='#'])))

