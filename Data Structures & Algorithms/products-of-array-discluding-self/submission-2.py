class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        postfix = 1

        res = [1] * len(nums)

        for i in range(len(nums) - 1):
            prefix *= nums[i]
            res[i + 1] = prefix

        for i in range(len(nums) - 1, 0 , -1):
            postfix *= nums[i]
            res[i - 1] *= postfix

        return res