class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = prices[0]

        profit = 0

        for i in prices:
            profit = max(profit, i - p)
            p = min(i, p)


        return profit