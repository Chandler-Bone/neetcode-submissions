class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = []
        for i in count.values():
            if i != 0:
                heapq.heappush_max(max_heap, i)

        cycles = 0
        queue = deque([])
        while max_heap or queue:
            cycles += 1
            if max_heap:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt:
                    queue.append((cnt, cycles + n))

            if queue and queue[0][1] == cycles:
                heapq.heappush_max(max_heap, queue.popleft()[0])


        # print(max_heap)

        return cycles