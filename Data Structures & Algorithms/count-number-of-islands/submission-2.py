class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COMPASS = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )

        def dfs(i, j):
            grid[i][j] = "0"
            for di, dj in COMPASS:
                if i+di >= 0 and i+di < len(grid) and j+dj >= 0 and j+dj < len(grid[0]) and grid[i+di][j+dj] == "1":
                    dfs(i+di, j+dj)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count
