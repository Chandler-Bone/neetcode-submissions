class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = []

        def dfs(i, arr):
            # print(i)
            # print(arr)
            if len(arr) == len(nums):
                permutations.append(arr.copy())
                return
            
            for ai in range(len(arr) + 1):
                # print("array index - "+ str(ai))
                arr.insert(ai, nums[i])
                dfs(i + 1, arr)
                del arr[ai]

        dfs(1, [nums[0]])
                
        return permutations
