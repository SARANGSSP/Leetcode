class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxprofit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]    
            if prices[i] > sell:
                sell = prices[i]
            profit = sell - buy
            maxprofit = max(maxprofit,profit)
        return maxprofit
            

