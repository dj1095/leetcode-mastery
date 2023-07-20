class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {key:[] for key in range(numCourses)}
        for course,preReq in prerequisites:
            preMap[course].append(preReq)

    #To check if there are any cycles in the graph
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True
            visit.add(course)
            for preReq in preMap[course]:
                if not dfs(preReq):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        