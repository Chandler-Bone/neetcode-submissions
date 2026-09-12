class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if target % 1 != 0:
            return False

        dp = set([0])

        for i in nums:
            for j in list(dp):
                dp.add(j + i)

            dp.add(i)

            if target in dp:
                return True
        
        return False
                