class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        buy = prices[0]
        max_profit = 0
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            profit = prices[i] - buy
            max_profit = max(max_profit,profit)
        return max_profit 




