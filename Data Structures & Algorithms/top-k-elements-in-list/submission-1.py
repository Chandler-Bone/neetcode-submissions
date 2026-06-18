class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] += 1
        
        for num, x in count.items():
            freq[x].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res

        return res