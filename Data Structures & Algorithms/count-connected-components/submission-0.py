class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = {i:set() for i in range(n)}

        for node, cnode in edges:
            adj_map[node].add(cnode)
            adj_map[cnode].add(node)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            for cnode in adj_map[node]:
                if cnode not in visited:
                    dfs(cnode)

        count = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            count += 1
        
        return count