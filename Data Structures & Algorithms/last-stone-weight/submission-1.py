class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            big_rock = heapq.heappop_max(heap)
            lil_rock = heapq.heappop_max(heap)

            if big_rock - lil_rock != 0:
                heapq.heappush_max(heap, big_rock - lil_rock)

        return heap[0] if len(heap) == 1 else 0