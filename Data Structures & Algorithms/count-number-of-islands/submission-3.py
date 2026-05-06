class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COMPASS = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        )

        def sink(i, j):
            grid[i][j] = "0"
            
            for di, dj in COMPASS:
                if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[i]) and grid[i+di][j+dj] == "1":
                    sink(i+di, j+dj)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    sink(i, j)
        return count
