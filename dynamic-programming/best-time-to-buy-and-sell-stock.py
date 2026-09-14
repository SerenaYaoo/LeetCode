class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            curr_price = prices[i]
            for j in range(i, len(prices)):
                curr_diff = prices[j] - curr_price
                if curr_diff > max_profit:
                    max_profit = curr_diff
        return max_profit
            
            
        