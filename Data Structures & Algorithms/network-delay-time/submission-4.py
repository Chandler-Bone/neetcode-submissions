class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)

        for src, tgt, time in times:
            adj_list[src].append((tgt, time))
        
        print(adj_list)
        visited = set()
        min_heap = [(0, k)]
        curr_time = 0

        while min_heap and len(visited) != n:
            # print(curr_time)
            # print(min_heap)
            curr_time = min_heap[0][0]

            while min_heap and curr_time == min_heap[0][0]:
                # print(min_heap)
                curr_node = heapq.heappop(min_heap)
                if curr_node[1] in visited:
                    continue
                visited.add(curr_node[1])
                # print(curr_node[1])
                # print(curr_time)
                for tgt_node, time in adj_list[curr_node[1]]:
                    if tgt_node not in visited:
                        heapq.heappush(min_heap, (curr_time + time, tgt_node))

            # print(visited)
            
        return -1 if len(visited) != n else curr_time