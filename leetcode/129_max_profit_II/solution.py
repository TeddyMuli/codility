class Solution:
    def maxProfit(self, prices):
        profit = 0
        candidate = prices[0]

        for price in prices[1:]:
            if price - candidate > 0:
                profit += price - candidate
            candidate = price

        return profit
