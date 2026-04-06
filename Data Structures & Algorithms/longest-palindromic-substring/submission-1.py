class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l, max_r = 0, 0

        for i in range(len(s)):
            l, r = i, i
            while l > 0 and r < len(s) - 1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            if r - l > max_r - max_l:
                max_l, max_r = l, r

            if i + 1 < len(s) and s[i] == s[i+1]:
                l, r = i, i + 1
                while l > 0 and r < len(s) - 1 and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                if r - l > max_r - max_l:
                    max_l, max_r = l, r

        return s[max_l:max_r+1]
