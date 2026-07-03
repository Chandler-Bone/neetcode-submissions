class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_nums = set(nums)
        res = 0


        for i in set_nums:
            
            if i + 1 not in set_nums:
                count = 1
                while i - count in set_nums:
                    count += 1
                res = max(res, count)

        return res