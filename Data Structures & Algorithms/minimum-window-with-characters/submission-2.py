from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts, window = Counter(t), defaultdict(int)

        have, need = 0, len(counts)
        ml, mr, longest = -1, -1, len(s) + 1
        l = r = 0
        while r < len(s):
            window[s[r]] += 1
            if s[r] in counts and window[s[r]] == counts[s[r]]:
                have += 1
            r += 1
            
            while have == need:
                if r - l < longest:
                    ml, mr, longest = l, r, r - l
                
                window[s[l]] -= 1
                if s[l] in counts and window[s[l]] < counts[s[l]]:
                    have -= 1
                l += 1
        
        return s[ml:mr]
