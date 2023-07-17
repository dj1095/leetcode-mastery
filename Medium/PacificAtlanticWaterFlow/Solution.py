class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights) , len(heights[0])
        pac, atl = set() , set()

        def dfs(r,c,prevHeight, visit):
            if ( r not in range(0, ROWS) or
                c not in range(0, COLS) or
                heights[r][c] < prevHeight or
                (r,c) in visit):
                return
            visit.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visit)
            

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)
        return list(pac.intersection(atl))
