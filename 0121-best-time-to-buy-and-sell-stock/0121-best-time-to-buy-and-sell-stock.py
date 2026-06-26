class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        least = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            price = prices[i]
            if price<least:
                least = price
            elif price-least > profit:
                profit = price-least
        return profit