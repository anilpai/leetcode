# Time complexity: O(log(min(m,n)))
# Space complexity: O(1)

# https://www.youtube.com/watch?v=LPFhl65R7ww&t=487s


class Solution:
    def median(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        i_min, i_max, half_len = 0, m, (m+n+1)/2
        while i_min <= i_max:
            i = (i_min + i_max)/2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is small, so must increase
                i_min = i+1
            elif i > 0 and A[i-1] > B[j]:
                # i is big, so must decrease
                i_max = i-1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])

                if (m+n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


if __name__=='__main__':
    s = Solution()
    A = [1, 2]
    B = [3, 4]
    print(s.median(A, B))
    A = [900]
    B = [5, 8, 10, 20]
    print(s.median(A, B))
    A = [23, 26, 31, 35]
    B = [3, 5, 7, 9, 11, 16]
    print(s.median(A, B))
