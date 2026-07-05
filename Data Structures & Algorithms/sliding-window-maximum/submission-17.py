class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        max_q = deque()
        res = []
        
        l = 0
        r = 0
        while r < len(nums):
            while max_q and nums[max_q[-1]] < nums[r]:
                max_q.pop()

            max_q.append(r)

            if l > max_q[0]:
                max_q.popleft()

            if r >= k - 1:
                res.append(nums[max_q[0]])
                l += 1
            r += 1

        # print(res)


        return res