class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        least = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<least:
                least=prices[i]
            elif prices[i]-least > profit:
                profit=prices[i]-least
        return profit