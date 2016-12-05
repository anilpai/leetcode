from collections import Counter


class Solution(object):
    def rearrangeString(self, str, k):
        """
        Rearrange Strings K Distance Apart.

        Characters Atleast K distances away. Wont handle Exactly K distance away.
        """

        c = Counter(str)

        max_cnt = c.most_common(1)[0][1]

        blocks = [[] for _ in range(max_cnt)]

        i = 0
        for cnt in c.most_common():
            for _ in range(cnt[1]):
                blocks[i].append(cnt[0])
                i = (i + 1) % max(cnt[1], max_cnt - 1)

        for i in range(max_cnt-1):
            if len(blocks[i]) < k:
                return ''

        return ''.join(map(lambda x: ''.join(x), blocks))


if __name__=='__main__':
    s = Solution()
    st = 'xyzaaabbcccdd'
    print(s.rearrangeString(st, 3))
    print(s.rearrangeString(st, 4))
    print(s.rearrangeString(st, 5))
    if s.rearrangeString(st, 6) == '':
        print("Not possible")