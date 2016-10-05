
class Solution(object):

    def __init__(self):
        '''
        Initialize the ones and tens position array.
        '''
        self.ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
            "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
        self.tens = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

    def num2word(self, n, s):
        '''
        Converts a 3 digit number into hundred , ten and ones .
        :param n: an integer number upto 3 digits.
        :param s: placeholder string.
        :return: a word string.
        '''
        str = ''

        h = int(n / 100) % 100
        n %= 100
        if h > 0:
            str += self.ones[h] + "hundred "

        if n > 19:
            str += self.tens[int(n/10)] + self.ones[int(n%10)]
        else:
            str += self.ones[int(n)]

        # If N is not zero
        if n:
            str += s

        return str

    def convert2word(self, n):
        word = ''
        # trillionth place
        word += self.num2word(int(n / 1000000000000), "trillion ")
        # billionth place
        word += self.num2word(int((n / 1000000000) % 1000), "billion ")
        # millionth place
        word += self.num2word(int((n / 1000000) % 1000), "million ")
        # thousandth place
        word += self.num2word(int((n / 1000) % 1000), "thousand ")
        # hundredth place
        word += self.num2word(int((n / 100) % 10), "hundred ")

        if n > 100 and n % 100:
            word += "and "

        word += self.num2word((n % 100), "")

        return word


if __name__ == '__main__':
    s = Solution()
    n = 5129038237764
    print(s.convert2word(n))