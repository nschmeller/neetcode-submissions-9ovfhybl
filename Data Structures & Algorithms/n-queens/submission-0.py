class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posd, negd = set(), set(), set()
        board, res = [["."] * n for i in range(n)], []

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
            else:
                for c in range(n):
                    if not (c in cols or r+c in posd or r-c in negd):
                        board[r][c] = "Q"
                        cols.add(c); posd.add(r+c); negd.add(r-c)

                        backtrack(r+1)

                        board[r][c] = "."
                        cols.remove(c); posd.remove(r+c); negd.remove(r-c)

        backtrack(0)
        return res
