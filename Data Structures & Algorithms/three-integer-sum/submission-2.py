class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for a, i in enumerate(nums):
            
            if(a > 0) and (nums[a] == nums[a-1]):
                continue

            b = a + 1
            c = len(nums) - 1

            while b < c:
                if(b > a + 1) and (nums[b] == nums[b-1]):
                    b += 1
                    continue
                if (c < len(nums) - 2) and (nums[c] == nums[c+1]):
                   c -= 1
                   continue

                sum_nums = nums[a] + nums[b] + nums[c]

                if sum_nums > 0:
                    c -= 1
                    continue
                if sum_nums < 0:
                    b += 1
                    continue

                res.append([nums[a], nums[b], nums[c]])
                b += 1
            
            
        return res 