#
# class Solution(object):
#
#     def ladderLength(self, start, end, dict):
#         q = []
#         q.append((start, 1))
#         while q:
#             curr = q.pop(0)
#             currword = curr[0]
#             currlen = curr[1]
#             if currword == end:
#                 return currlen
#             for i in range(len(start)):
#                 part1 = currword[:i]
#                 part2 = currword[i+1:]
#                 for j in 'abcdefghijklmnopqrstuvwxyz':
#                     if currword[i] != j:
#                         nextword = part1 + j + part2
#                         if nextword in dict and nextword not in q:
#                             q.append((nextword, currlen+1))
#         return 0
#
# if __name__=='__main__':
#     s = Solution()
#     start = "hit"
#     end = "cog"
#     dict = ["hot", "dot", "dog", "lot", "log"]
#     print(s.ladderLength(start, end, dict))