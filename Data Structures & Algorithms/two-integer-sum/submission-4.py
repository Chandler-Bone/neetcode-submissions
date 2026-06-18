class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_idx = dict()

        for idx, n in enumerate(nums):
            nums_idx[n] = idx

        for idx, n in enumerate(nums):
            target_num = target - n
            if(target_num in nums_idx and idx != nums_idx[target_num]):
                return [idx, nums_idx[target_num]]

        return [-1,-1]

        