class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_fish = 0
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        q = collections.deque()

        def bfs(r,c):
            max_fish_count = grid[r][c]
            directions = [(0,1) , (0,-1), (1,0), (-1,0)]
            q.append((r,c))
            while q:
                r1, c1 = q.popleft()
                for dr, dc in directions:
                    newRowIdx = r1 + dr
                    newColIdx = c1 + dc
                    if newRowIdx in range(0,rows) and newColIdx in range(0,cols) and (newRowIdx,newColIdx) not in visited and grid[newRowIdx][newColIdx] > 0:
                        q.append((newRowIdx,newColIdx))
                        visited.add((newRowIdx,newColIdx))
                        max_fish_count += grid[newRowIdx][newColIdx]
            return max_fish_count
                
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] > 0 :
                    visited.add((r,c))
                    max_fish = max(max_fish, bfs(r,c))
        return max_fish