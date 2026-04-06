from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        t_counts, window = Counter(t), defaultdict(int)
        have, need = 0, len(t_counts)
        res, res_length = (-1, -1), float('inf')

        l = 0
        for r, c in enumerate(s):
            window[c] += 1

            if c in t_counts and window[c] == t_counts[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_length:
                    res = (l, r)
                    res_length = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in t_counts and window[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_length != float('inf') else ""
