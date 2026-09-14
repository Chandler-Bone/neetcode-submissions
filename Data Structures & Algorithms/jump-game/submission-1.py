class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0:
            return len(nums) == 1

        p_ri = len(nums) - 1

        while p_ri != 0:
            
            p_le = p_ri - 1

            while p_le >= 0:
                dist = p_ri - p_le
                if(nums[p_le] >= dist):
                    p_ri = p_le
                    break

                p_le -= 1
            
            if p_le == -1:
                return False

        return True