class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {key:[] for key in range(numCourses)}
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)
        cycle , visit= set() , set()
        ordering = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            ordering.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ordering