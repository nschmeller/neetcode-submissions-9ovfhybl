class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COMPASS = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def backtrack(i, j, curr):
            print(i, j, curr)
            if curr == len(word) - 1 and board[i][j] == word[curr]:
                print("trued")
                return True
            elif board[i][j] != word[curr]:
                print("falsed")
                return False
            else:
                visited[i][j] = True
                res = any([
                    backtrack(i+di, j+dj, curr+1)
                    for di, dj in COMPASS
                    if i+di >= 0 and i+di < len(board) and j+dj >= 0 and j+dj < len(board[0]) and not visited[i+di][j+dj]
                ])
                visited[i][j] = False
                return res
        
        return any([backtrack(i, j, 0) for i in range(len(board)) for j in range(len(board[i]))])
