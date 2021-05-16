class Solution:
    def surfaceArea(self, grid):
        sz=len(grid)
        vic=0
        for i in range(sz):
            for j in range(sz):
                
                if grid[i][j]>0:
                    vic+=(4*grid[i][j]+2)
                
                if (j>0):
                    vic-=min(grid[i][j],grid[i][j-1])*2
                if (i>0):
                    vic-=min(grid[i][j],grid[i-1][j])*2
        return vic            
   

        