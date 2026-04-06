class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = (r + l) // 2
            mi, mj = mid // COLS, mid % COLS
            if target < matrix[mi][mj]:
                r = mid - 1
            elif target > matrix[mi][mj]:
                l = mid + 1
            else:
                return True

        return False
