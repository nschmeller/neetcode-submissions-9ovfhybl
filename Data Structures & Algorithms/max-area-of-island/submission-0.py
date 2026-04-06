class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        COMPASS = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        )

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + sum(
                    [
                        dfs(i+di, j+dj)
                        for di, dj in COMPASS
                        if i+di >= 0 and i+di < len(grid) and j+dj >= 0 and j+dj < len(grid[0])
                    ]
                )
        
        return max([dfs(i, j) for i in range(len(grid)) for j in range(len(grid[i]))])
