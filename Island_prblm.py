def island(grid):
    if not grid:
        return 0
    rows=len(grid)
    cols=len(grid[0])
    visit = set()

    def dfs(r , c):
        if r<0 and r<=rows or c<0 or c<=cols or grid[r][c] == "0" or (r,c) in visit:
            return visit.add((r,c))

        dfs(r,c-1)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r+1,c)
    island_count=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] =="1" and (r,c) not in visit:
                dfs(r,c)
                island_count= 1
    return island_count
grid = [["1" , "1" , "1" , "1" , "0"],
        ["1" , "1" , "0" , "1" , "0"],
        ["1" , "1" , "0" , "0" , "0"],
        ["0" , "0" , "0" , "0" , "0"]
        ]
print(island(grid))
    
                
            
                
                
        
        
