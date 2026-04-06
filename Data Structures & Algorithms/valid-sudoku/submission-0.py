class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def invalid(group):
            seen = set()
            for num in group:
                if num != ".":
                    if num in seen:
                        return True
                    else:
                        seen.add(num)

        if any(invalid(row) for row in board):
            return False
        
        if any(invalid(col) for col in zip(*board)):
            return False
        
        if any(invalid([board[k + i*3][l + j*3] for k in range(3) for l in range(3)]) for i in range(3) for j in range(3)):
            return False
        
        return True
