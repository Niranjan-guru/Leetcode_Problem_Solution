class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyStock = float("inf")
        profit = 0

        for i in prices:
            buyStock = min(buyStock, i)
            profit = max(profit, i - buyStock)
        return profit