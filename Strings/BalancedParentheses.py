from utils.timer import timing


class Solution(object):

    def __init__(self):
        self.opening = '({['
        self.closing = ')}]'

    @timing
    def paranthesisChecker(self, str):

        s = []
        flag = True
        i = 0

        while i < len(str) and flag:
            if str[i] in self.opening:
                s.append(str[i])
            else:
                if len(s) == 0:
                    flag = False
                else:
                    top = s.pop()
                    if not (self.opening.index(top) == self.closing.index(str[i])):
                        flag = False
            i += 1
        if flag and len(s) == 0:
            print("YES")
            return True
        else:
            print("NO")
            return False

if __name__ == '__main__':
    strings = ['{{([][])}()}', '[{()]']
    s = Solution()
    print("String is : "+strings[0])
    print(s.paranthesisChecker(strings[0]))
    print("String is : "+strings[1])
    print(s.paranthesisChecker(strings[1]))
