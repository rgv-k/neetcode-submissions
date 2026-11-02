class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p, profit = prices[0], 0

        for i in prices:
            profit = max(profit, i - p)
            p = min(i, p)


        return profit