class Solution:
    def maxProfit(self, prices):
        profit = 0
        candidate = prices[0]

        for price in prices[1:]:
            if price - candidate > profit:
                profit = price - candidate
            elif price - candidate < 0:
                candidate = price

        return profit
