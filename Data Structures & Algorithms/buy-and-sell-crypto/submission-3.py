class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for price in prices[1:]:
            buy, profit = min(buy, price), max(profit, price - buy)
        return profit
