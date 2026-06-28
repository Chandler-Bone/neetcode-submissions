class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            print(l)
            print(r)
            print(m)
            print("+++")

            if(nums[m] == target):
                return m

            if(nums[l] <= nums[m]):
                #left sorted array
                if nums[l] <= target and target < nums[m]:
                    #if target is within nums[l] and num[r] on left side
                    r = m - 1
                else:
                    l = m + 1
            else:
                #right sorted array
                if nums[m] < target and target <= nums[r]:
                    #if target is within nums[m] and nums[r] on the right side
                    l = m + 1
                else:
                    r = m - 1

        return -1