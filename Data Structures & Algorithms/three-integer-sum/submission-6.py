class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        a = 0

        while a < len(nums) - 2:

            if a > 0 and nums[a-1] == nums[a]:
                a += 1
                continue

            b = a + 1
            c = len(nums) - 1

            while b < c:
                if b > a + 1 and nums[b-1] == nums[b]:
                    b+=1
                    continue
                if c < len(nums) - 1 and nums[c+1] == nums[c]:
                    c-=1
                    continue

                n_sum = nums[a] + nums[b] + nums[c]
                if(n_sum < 0):
                    b += 1
                elif(n_sum > 0):
                    c -= 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1

            a += 1

        return res