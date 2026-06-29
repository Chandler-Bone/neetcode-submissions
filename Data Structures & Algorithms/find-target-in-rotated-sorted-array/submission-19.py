class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                #left side sorted, also middle as 2 size defaults to left
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #right side is sorted
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1