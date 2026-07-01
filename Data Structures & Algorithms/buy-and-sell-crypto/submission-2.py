class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_val = 0
        low_price = prices[0]

        for i in prices:
            low_price = min(low_price, i)
            max_val = max(max_val, i - low_price)

        return max_val