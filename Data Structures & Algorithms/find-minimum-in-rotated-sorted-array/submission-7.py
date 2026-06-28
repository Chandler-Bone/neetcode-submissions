class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:            
            m = l + (r - l) // 2

            # print(l)
            # print(r)
            # print(m)
            # print("++")

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]

