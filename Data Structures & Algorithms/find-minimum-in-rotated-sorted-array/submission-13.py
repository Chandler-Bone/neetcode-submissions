class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            print(l)
            print(r)
            print(m)
            print("+++")

            if nums[m] < nums[r]:
                #we know the right side is sorted and unneeded the min wont be here
                # we dont know if the mid is the lowest point or not
                r = m
            else:
                #if the left side is sorted, then our min wont be here skip over
                #we dont care if the largest point is there, we skip over it
                l = m + 1


        return nums[l]