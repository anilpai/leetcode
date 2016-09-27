import bisect
import random
import timeit

# Reset the seed
random.seed(1)

# Use bisect_left and insort_left.
l = []

start_time = timeit.default_timer()
for i in range(1, 20000):
    r = random.randint(1, 5000)
    position = bisect.bisect_left(l, r)
    bisect.insort_left(l, r)
    # print(l)

elapsed = timeit.default_timer() - start_time
print(elapsed)  # 0.008461000004899688


start_time = timeit.default_timer()

a = [random.randint(1, 5000) for i in range(20000)]
for x in a:
    if x in a:
        pass
        #print("True")
    else:
        pass
        #print("False")

elapsed = timeit.default_timer() - start_time
print(elapsed)  # 0.05278499999985797


start_time = timeit.default_timer()

a = [random.randint(1, 5000) for i in range(20000)]

for x in a:
    lo = 0
    hi = 18
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            pass
            #print("True")
            lo = hi

elapsed = timeit.default_timer() - start_time
print(elapsed)