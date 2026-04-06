from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            counts = tuple(sorted(Counter(s).items()))
            groups[counts].append(s)
        
        return list(groups.values())
