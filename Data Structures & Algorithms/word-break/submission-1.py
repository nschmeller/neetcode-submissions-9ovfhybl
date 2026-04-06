from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def segment(start, end):
            if end == len(s) and s[start:end] in wordDict:
                return True
            elif end > len(s):
                return False
            elif s[start:end] in wordDict:
                return segment(end, end+1) or segment(start, end+1)
            else:
                return segment(start, end+1)

        return segment(0, 1)
