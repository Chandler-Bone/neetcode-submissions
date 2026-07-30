class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for i in tasks:
            count[ord(i) - ord('A')] += 1
        
        max_heap = []

        for i in count:
            if i != 0:
                heapq.heappush_max(max_heap, i)

        queue = deque([])
        cycles = 0
        while max_heap or queue:
            print(max_heap)
            if max_heap:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt != 0:
                    queue.append((cnt, cycles + n))
            print(max_heap)
            if queue and queue[0][1] == cycles:
                cnt, _ = queue.popleft()
                heapq.heappush_max(max_heap, cnt)
            
            cycles += 1

        return cycles