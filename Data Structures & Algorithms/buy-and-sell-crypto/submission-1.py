class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = float('inf'), 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit
        