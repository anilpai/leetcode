class Solution(object):

    def flatten(self, l, a):
        for i in l:
            if isinstance(i, list):
                self.flatten(i, a)
            else:
                a.append(i)
        return a


    def merge(self, a, b):
        i = j = k = 0
        t =[]
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                t.append(a[i])
                i+=1
            else:
                t.append(b[j])
                j+=1

        while i < len(a):
            t.append(a[i])
            i+=1

        while j < len(b):
            t.append(b[j])
            j+=1

        return t

    def pushToZero(self, arr, n):
        count = 0
        for i in range(0, n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < n:
            arr[count] = 0
            count += 1
        return arr


    def printIntegerVertically(self, i):
        r = i % 10
        if r == 0:
            return
        else:
            self.printIntegerVertically(int(i/10))
        print(r)


    def reverseTheInteger(self, i):
        r = 0
        while i != 0:
            r *= 10
            r += i%10
            i = int(i/10)
        return r


if __name__=='__main__':
    s = Solution()
    # To push all the zeroes to the right.
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    print(s.pushToZero(arr, n))

    # To flatten a list of lists
    print(s.flatten([[[1, [1,1, [3, [4,5,]]]], 2, 3], [4, 5],6], []))

    # To merge two lists
    a = [1, 7, 9, 10, 14, 17, 20, 22]
    b = [2, 3, 4, 6, 8, 11, 15, 21]

    print(s.merge(a, b))

    # To print an integer vertically
    s.printIntegerVertically(1234)

    # To reverse an integer
    print(s.reverseTheInteger(12345))

