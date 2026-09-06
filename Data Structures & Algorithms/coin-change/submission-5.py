class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        min_amounts = {i:10001 for i in range(amount + 1)}
        min_amounts[0] = 0

        for amt in range(amount + 1):
            for c in coins:
                if amt - c >= 0:
                    min_amounts[amt] = min(min_amounts[amt], min_amounts[amt - c] + 1)

        return min_amounts[amount] if min_amounts[amount] != 10001 else -1