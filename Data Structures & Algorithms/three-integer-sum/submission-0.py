class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        nums.sort()
        print(nums)
        for a, i in enumerate(nums):
            if a > 0 and i == nums[a - 1]:
                continue
            
            b = a + 1
            c = len(nums) - 1
            # print(i)
            while b < c:
                # print("a"+str(a)+"b"+str(b)+"c"+str(c))
                if b > a + 1 and nums[b] == nums[b-1]:
                    b += 1
                    continue
                if c < len(nums) - 2 and nums[c] == nums[c+1]:
                    c -= 1
                    continue
                
                if nums[a] + nums[b] + nums[c] > 0:
                    c -= 1
                    continue
                if nums[a] + nums[b] + nums[c] < 0:
                    b += 1
                    continue

                res.append([nums[a],nums[b],nums[c]])
                b += 1
            
        return res