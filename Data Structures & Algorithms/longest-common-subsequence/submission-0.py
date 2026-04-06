from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def sub(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + sub(i+1, j+1)
            else:
                return max(sub(i+1, j), sub(i, j+1))

        return sub(0, 0)
