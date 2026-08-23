class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i:[] for i in range(n)}

        for node, cnode in edges:
            adj_map[node].append(cnode)
            adj_map[cnode].append(node)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            if adj_map[node] == []:
                return

            visited.add(node)
            for cnode in adj_map[node]:
                if cnode != parent:
                    dfs(cnode, node)


        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, i)
                count += 1

        return count