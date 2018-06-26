import re

"""
Shunting Yard Algorithm is a classic algorithm for parsing mathematical expressions.
"""


class Solution(object):
    """ use of a stack to rearrange the operators and operands into the correct order for evaluation,
    which is rather reminiscent of a railway siding.
    """
    def is_number(self, str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    def e(self, str):
        a = map(int, re.split(r'\D', str))
        b = re.findall(r'[+/*-]', str)
        if b[0] == '+':
            return a[0] + a[1]
        elif b[0] == '-':
            return a[0] - a[1]
        elif b[0] == '*':
            return a[0] * a[1]
        elif b[0] == '/':
            return a[0] / a[1]

    def peek(self, stack):
        return stack[-1] if stack else None

    def apply_operator(self, operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        values.append(self.e("{0}{1}{2}".format(left,operator,right)))

    def greater_precedence(self, op1, op2):
        precedences = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1
        }
        return precedences[op1] > precedences[op2]

    def evaluate(self, expression):
        """a classic algorithm for parsing mathematical expressions"""
        tokens = re.findall("[+*/()-]|\d+", expression)
        values = []
        operators = []
        for token in tokens:
            if self.is_number(token):
                values.append(int(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                top = self.peek(operators)
                while top is not None and top != '(':
                    self.apply_operator(operators, values)
                    top = self.peek(operators)
                operators.pop()
            else:
                # Operator
                top = self.peek(operators)
                while top is not None and top not in "()" and self.greater_precedence(top,token):
                    self.apply_operator(operators, values)
                    top = self.peek(operators)
                operators.append(token)
        while self.peek(operators) is not None:
            self.apply_operator(operators, values)

        return values[0]


if __name__=='__main__':
    s = Solution()
    expression = '((20 - 10 ) * (30 - 20) / 10 + 10 ) * 2'
    print("Shunting Yard Algorithm: {0}".format(s.evaluate(expression)))