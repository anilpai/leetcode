

class Solution(object):
    def matcher(self, open, close):
        opening = '({['
        closing = ')}]'
        return opening.index(open) == closing.index(close)

    def paranthesisChecker(self, str):

        # Initialize a Stack
        # By default, set the checker flag to true
        s = []
        flag = True
        i = 0

        while i < len(str) and flag:
            if str[i] in "([{":
                s.append(str[i])
            else:
                if len(s) == 0:
                    flag = False
                else:
                    top = s.pop()
                    if not self.matcher(top, str[i]):
                        flag = False
            i += 1
        if flag and len(s) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    strings = ['{{([][])}()}', '[{()]']
    s = Solution()
    print("String is : "+strings[0])
    print(s.paranthesisChecker(strings[0]))
    print("String is : "+strings[1])
    print(s.paranthesisChecker(strings[1]))
