class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_map = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            adj_map[crs].append(preq)

        print(adj_map)
        visited = set()
        def dfs(node):
            # print(node)
            if node in visited:
                # print("test1")
                return False
            if adj_map[node] == []:
                return True

            visited.add(node)
            for preq in adj_map[node]:
                if not dfs(preq):
                    # print("test2")
                    return False
            
            visited.remove(node)
            adj_map[node] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True