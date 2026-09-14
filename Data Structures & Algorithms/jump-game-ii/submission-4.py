class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums) - 1

        cost = [float('inf')] * len(nums)
        cost[0] = 0

        for i in range(len(nums) - 1):

            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums):
                    break
                
                cost[j] = min(cost[j], cost[i] + 1)

        print(cost)
        return cost[-1]