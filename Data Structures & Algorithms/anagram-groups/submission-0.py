from collections import defaultdict

class Solution:

    BASE = ord('a')

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for item in strs:
            counts = [0] * 26
            for c in item:
                counts[ord(c) - self.BASE] += 1
            anagrams[tuple(counts)].append(item)
        
        return [anagrams[anagram] for anagram in anagrams]
