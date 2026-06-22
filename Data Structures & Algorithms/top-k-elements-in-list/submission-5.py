class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, ct in count.items():
            freq[ct].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if(len(res) == k):
                    return res

        return res