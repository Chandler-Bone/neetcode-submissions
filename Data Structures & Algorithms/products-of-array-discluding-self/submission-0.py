class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = []

        p = 1

        for i in nums:
            p *= i
            prefix.append(p)
        
        p = 1
        for j in range(len(nums) - 1, -1, -1):
            p *= nums[j]
            postfix.insert(0,p)

        print(prefix)
        print(postfix)

        res = []
        # return res
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[1])
            elif i == len(nums) - 1:
                res.append(prefix[len(nums)-2])
            else:
                res.append(prefix[i-1] * postfix[i+1])

        return res