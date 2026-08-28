class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        val1 = nums[0]
        val2 = nums[1]

        for i in range(2, len(nums)):
            print(f"one: {val1}, two: {val2}, nums[{nums[i]}]")
            prev = val1
            if val1 + nums[i] > val2:
                temp = val2
                val2 = val1 + nums[i]
                val1 = temp
            else:
                val1 = val2
            if prev > val1:
                val1 = prev

        print(f"one: {val1}, two: {val2}")
        return max(val1, val2)