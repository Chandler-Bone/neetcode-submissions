class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        max_count = 0
        
        for i in nums_set:
            if i-1 in nums_set:
                continue
            
            j = i + 1
            count = 1
            while j in nums_set:
                count += 1
                j += 1
            
            max_count = max(max_count, count)
            
        return max_count

