from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(curr[j+1], prev[j])
            prev, curr = curr, prev
        
        return prev[0]
        




        # @cache
        # def sub(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     elif text1[i] == text2[j]:
        #         return 1 + sub(i+1, j+1)
        #     else:
        #         return max(sub(i+1, j), sub(i, j+1))

        # return sub(0, 0)
