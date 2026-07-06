class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = dict()

        for i, n in enumerate(nums):
            target_diff = target - n
            
            if target_diff in num_map:
                return [num_map[target_diff], i]
            
            num_map[n] = i

        return [-1,-1]