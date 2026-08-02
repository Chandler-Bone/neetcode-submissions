class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        def dfs(i, curr):
            if i == len(nums):
                res.add(tuple(curr))
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])

        return [list(i) for i in res]