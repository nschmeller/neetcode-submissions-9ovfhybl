class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # switch zeroes to sentinel value
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[row][col] = "zero"
        
        # set non-zero elements in zeroed rows / columns to 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "zero":
                    # zero out row
                    for i in range(m):
                        if matrix[i][col] != "zero":
                            matrix[i][col] = 0
                    for j in range(n):
                        if matrix[row][j] != "zero":
                            matrix[row][j] = 0
        
        # restore the original zeroes
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "zero":
                    matrix[row][col] = 0
