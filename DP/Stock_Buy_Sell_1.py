'''

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Input: [7, 1, 5, 3, 6, 4]
Output: 5

Input: [7, 6, 4, 3, 1]
Output: 0

'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit2(self, prices):
        '''
        Kadane's algorithm.
        '''
        maxCur = 0
        maxSoFar = 0
        for i in range(1, len(prices)):
            maxCur = max(0, maxCur + prices[i] - prices[i-1])
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar


if __name__=='__main__':
    s = Solution()
    transaction1 = [7, 1, 5, 3, 6, 4]
    transaction2 = [7, 6, 4, 3, 1]
    print(s.maxProfit(transaction1))
    print(s.maxProfit(transaction2))
    print(s.maxProfit2(transaction1))
    print(s.maxProfit2(transaction2))
    t3 = [1, 7, 4, 11]
    t4 = [0, 6, -3, 7]
    print (s.maxProfit2(t3))
    print (s.maxProfit2(t4))
