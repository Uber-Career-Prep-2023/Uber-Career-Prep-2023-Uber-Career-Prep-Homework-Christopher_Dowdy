'''
Inuition:
- if current cell in graph is an island, increment counter and call dfs function
    - dfs function should check adjacent cells and if they are an island, be set to '0' to be marked as visited
Technique: Graph DFS
TC: O(mxn) where m is the # of rows and n is # of cols
SC: O(mxn) where m is the # of rows and n is # of cols
'''

def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if grid[row][col] != "1":
            return
        grid[row][col] = "0"
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)
    count = 0 
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                dfs(row,col)
                count +=1
    return count

'''
Time spent: 7 mins
'''