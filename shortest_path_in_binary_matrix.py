from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0),
                (-1,-1),(1,1),(-1,1),(1,-1)]
        
        q = deque([(0, 0, 1)])
        grid[0][0] = 1
        
        while q:
            r, c, steps = q.popleft()
            
            if r == n-1 and c == n-1:
                return steps
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    q.append((nr, nc, steps + 1))
                    grid[nr][nc] = 1
        
        return -1