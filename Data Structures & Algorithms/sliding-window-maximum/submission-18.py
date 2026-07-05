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
                #while max_q has numbers and the latest number inserted is less that our current right
                # remove it. this is for cases such as when the queue [4,2] and nums[r] = 3
                max_q.pop()

            max_q.append(r)

            if l > max_q[0]:
                # if the index of the biggest number is smaller than l, we need to get rid of it
                max_q.popleft()

            if r >= k - 1:
                #once the window is wide enough we start appending and incrementing l
                res.append(nums[max_q[0]])
                l += 1
            r += 1


        return res