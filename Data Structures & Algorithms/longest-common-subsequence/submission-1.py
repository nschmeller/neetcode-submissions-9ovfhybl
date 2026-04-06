from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]
        




        # @cache
        # def sub(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     elif text1[i] == text2[j]:
        #         return 1 + sub(i+1, j+1)
        #     else:
        #         return max(sub(i+1, j), sub(i, j+1))

        # return sub(0, 0)
