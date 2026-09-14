class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_sum = nums[0]

        for n in range(1, len(nums)):
            if(curr_sum < 0):
                curr_sum = nums[n]
            else:
                curr_sum += nums[n]

            curr_max = max(curr_max, curr_sum)

        return curr_max