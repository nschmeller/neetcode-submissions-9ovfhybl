class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            if tuple(counts) in anagrams:
                anagrams[tuple(counts)].append(s)
            else:
                anagrams[tuple(counts)] = [s]
        
        return [anagrams[anagram] for anagram in anagrams]
