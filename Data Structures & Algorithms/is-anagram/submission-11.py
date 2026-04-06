class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        for c in s:
            s_counts[c] = 1 + s_counts.get(c, 0)
        
        t_counts = {}
        for c in t:
            t_counts[c] = 1 + t_counts.get(c, 0)
        
        return s_counts == t_counts
