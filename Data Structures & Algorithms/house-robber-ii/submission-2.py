class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        cache = [-1] * len(nums)

        def dfs(first, i):
            if i >= len(nums):
                return 0
            if first and i == len(nums) - 1:
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = max(nums[i] + dfs(first, i + 2), dfs(first, i + 1))
            return cache[i]

        val1 = dfs(False, 1)
        cache = [-1] * len(nums)
        val2 = dfs(True, 0)
        return max(val1 , val2)