class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        COMPASS = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )

        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in COMPASS:
                if 0 <= i+di < len(heights) and 0 <= j+dj < len(heights[0]) and (i+di, j+dj) not in visited and heights[i+di][j+dj] >= heights[i][j]:
                    dfs(i+di, j+dj, visited)
        
        pacific, atlantic = set(), set()

        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0])-1, atlantic)
        for j in range(len(heights[0])):
            dfs(0, j, pacific)
            dfs(len(heights)-1, j, atlantic)
        
        return [
            [i, j]
            for i in range(len(heights))
            for j in range(len(heights[0]))
            if (i, j) in pacific and (i, j) in atlantic
        ]
