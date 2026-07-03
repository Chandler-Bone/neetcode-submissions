class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        i = 0

        while i < len(nums) - 2:
            
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1 
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1 
                    continue

                val_sum = nums[i] + nums[j] + nums[k]

                if(val_sum == 0):
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif(val_sum < 0):
                    j += 1
                else:
                    k -= 1     

            i += 1

        return res

            
