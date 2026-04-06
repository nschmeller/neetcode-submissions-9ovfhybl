class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COMPASS = (
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
        )
        islands = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                for drow, dcol in COMPASS:
                    dfs(row + drow, col + dcol)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands
