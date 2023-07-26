class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        islandCount = 0
        #################### BFS ##########
        def bfs(r, c):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            q = collections.deque()
            q.append((r,c))
            while q:
                r , c = q.popleft()
                for dr, dc in directions:
                    r2 , c2= r + dr , c + dc
                    if (r2, c2) not in visited and r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == "1":
                        visited.add((r2,c2))
                        q.append((r2,c2))
        ###################END ###############
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    islandCount += 1
        return islandCount

