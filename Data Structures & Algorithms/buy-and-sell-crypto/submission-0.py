class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Verifying a redo to make sure i understood the concept of sliding window:
        profit = 0
        buy = 0 
        sell = 1
        while sell < len(prices):

            if prices[sell] < prices[buy]:
                buy = sell
            
            else:
                current_transaction = prices[sell] - prices[buy]
                profit = max(profit, current_transaction)

            sell += 1

        return profit
        