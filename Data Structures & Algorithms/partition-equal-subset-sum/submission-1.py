class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums) / 2

        possible_sums = set()

        for i in range(len(nums) - 1, -1, -1):
            
            for j in list(possible_sums):
                possible_sums.add(nums[i] + j)

            possible_sums.add(nums[i])

            print(possible_sums)    
            if target in possible_sums:
                return True
        
        return False