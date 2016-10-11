

# Fails for large cases.

def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n - 1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


y = partitions(54)
count = 0
while 1:
    try:
        print(next(y))
        count += 1
    except:
        print("Finished")
        break

print("Total Partitions: "+str(count))