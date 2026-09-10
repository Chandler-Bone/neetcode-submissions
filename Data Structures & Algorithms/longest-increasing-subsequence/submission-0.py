class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            
            cur_i_max = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cur_i_max = max(cur_i_max, counts[j] + 1)
            counts[i] = cur_i_max

        return max(counts)
