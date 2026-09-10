class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums) / 2

        def dfs(i, total):
            if i >= len(nums):
                return False
            
            if total == target:
                return True
            elif total > target:
                return False
            
            return dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

        return dfs(0,0)
