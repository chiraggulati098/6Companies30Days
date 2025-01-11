class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0 or k == 0:
            return 0

        buy_price = [float('inf')] * k
        profit = [float('-inf')] * k

        for price in prices:
            for i in range(k):
                buy_price[i] = min(buy_price[i], price - (profit[i - 1] if i > 0 else 0))
                profit[i] = max(profit[i], price - buy_price[i])
        
        return profit[k - 1]