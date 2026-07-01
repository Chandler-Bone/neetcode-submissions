class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_val = 0
        low_idx = 0

        for i in range(len(prices)):
            if(prices[i] < prices[low_idx]):
                low_idx = i

            max_val = max(max_val, prices[i] - prices[low_idx])

        return max_val