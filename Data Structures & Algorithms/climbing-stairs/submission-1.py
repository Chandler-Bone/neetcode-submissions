class Solution:
    def climbStairs(self, n: int) -> int:
        val1 = 1
        val2 = 1

        for i in range(n - 1):
            temp = val1
            val1 = val1 + val2
            val2 = temp

        return val1