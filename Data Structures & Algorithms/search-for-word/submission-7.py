class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COMPASS = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        )

        def explore(i, j, k, path):
            if k == len(word):
                return True
            elif not (0 <= i < len(board) and 0 <= j < len(board[0])) or (i, j) in path or word[k] != board[i][j]:
                return False
            else:
                path.add((i, j))
                found = any(
                    explore(i+di, j+dj, k+1, path)
                    for di, dj in COMPASS
                )
                path.remove((i, j))
                return found

        for i in range(len(board)):
            for j in range(len(board[i])):
                if explore(i, j, 0, set()):
                    return True

        return False
