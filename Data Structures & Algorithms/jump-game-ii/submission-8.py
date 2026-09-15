class Solution:
    def jump(self, nums: List[int]) -> int:

        i = 0
        count = 0
        while i < len(nums) - 1:
            # print(i)
            next_i = 0
            largest_jump = 0
            for j in range(i + 1, i + nums[i] + 1):
                if j == len(nums) - 1:
                    next_i = len(nums) - 1 
                    break
                if(j + nums[j] > largest_jump):
                    largest_jump = j + nums[j]
                    next_i = j
            
            count += 1
            i = next_i

        return count