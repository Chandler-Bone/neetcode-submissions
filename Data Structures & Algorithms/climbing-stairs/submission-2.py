class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        val1 = 1
        val2 = 2

        for i in range(2, n):
            temp = val2
            val2 = val1 + val2
            val1 = temp

        return val2