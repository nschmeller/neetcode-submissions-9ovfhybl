class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        for char in t:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
            else:
                return False

        for char in counts:
            if counts[char] > 0:
                return False

        return True
