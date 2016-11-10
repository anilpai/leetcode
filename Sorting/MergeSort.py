class Solution(object):
    '''
    NOT WORKING !!
    '''
    def mergesort(self, a, first, last):
        mid = (first + last)/2
        if first < last:
            self.mergesort(a, first, mid)
            self.mergesort(a, mid+1, last)
        i, f, l = 0, first, mid+1
        tmp = [None] * (last - first + 1)

        while f<=mid and l<=last:
            if a[f] < a[l]:
                tmp[i] = a[f]
                f += 1
            else:
                tmp[i] = a[l]
                l += 1
            i += 1

        if f <= mid:
            tmp[i:] = a[f:mid+1]

        if l <= last:
            tmp[i:] = a[l:last+1]

        i = 0
        while first <=last:
            a[first] = tmp[i]
            first += 1
            i += 1


if __name__=='__main__':
    s = Solution()
    a = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2]
    print(s.mergesort(a, 0, len(a)-1))