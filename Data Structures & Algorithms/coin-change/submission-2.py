class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        c_rems = [amount + 1] * (amount + 1)
        c_rems[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    c_rems[a] = min(c_rems[a], c_rems[a - c] + 1)

        return c_rems[amount] if c_rems[amount] != amount + 1 else -1