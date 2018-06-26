
'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
        # total = 0
        # for i in range(0, len(prices)-1):
        #     if prices[i+1] > prices[i]:
        #         total += prices[i+1]-prices[i]
        #
        # return total


if __name__=='__main__':
    s = Solution()
    transaction1 = [7, 1, 5, 3, 6, 4]
    transaction2 = [7, 6, 4, 3, 1]
    print(s.maxProfit(transaction1))
    print(s.maxProfit(transaction2))
