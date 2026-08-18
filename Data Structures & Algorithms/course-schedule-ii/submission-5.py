class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preqMap = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preqMap[crs].append(preq)

        res = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if preqMap[crs] == []:
                if crs not in visited:
                    res.append(crs)
                visited.add(crs)
                return True
            
            cycle.add(crs)

            for preq in preqMap[crs]:
                if not dfs(preq):
                    return False
            
            if crs not in visited:
                res.append(crs)
            visited.add(crs)
            cycle.remove(crs)
            preqMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res