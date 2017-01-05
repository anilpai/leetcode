
def findRoom(a, d, n):
    a.sort()
    d.sort()

    m_room = 1
    res = 1
    i = 1
    j = 0

    while i < n and j < n:
        if a[i] < d[j]:
            m_room+=1
            i+=1
            if m_room > res:
                res = m_room
        else:
            m_room-=1
            j+=1

    return res


if __name__=='__main__':
    a = [900, 940, 950, 1100, 1500, 1800]
    d = [910, 1200, 1120, 1130, 1900, 2000]
    n = len(a)
    print(findRoom(a, d, n))