class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        height=len(grid)
        width=len(grid[0])
        visited =set()
        islands=0
        
        def dfs(sr,sc):
            q=collections.deque()
            visited.add((sr,sc))
            q.append((sr,sc))
            while q:
                r,c=q.pop()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    sr,sc=r+dr,c+dc
                    if (sr in range(height) and sc in range (width) and grid[sr][sc]=="1" and ((sr,sc) not in visited)):
                                        visited.add((sr,sc))
                                        q.append((sr,sc))
            
        if not grid:
            return islands
        else:
            for r in range(height):
                for c in range(width):
                    if grid[r][c]=="1" and (r,c) not in visited:
                        dfs(r,c)
                        islands+=1
            return islands
        