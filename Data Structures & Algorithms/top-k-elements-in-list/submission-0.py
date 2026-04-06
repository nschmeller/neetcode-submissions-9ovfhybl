from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freqs = [[] for i in range(len(nums)+1)]
        for num, count in counts.items():
            freqs[count].append(num)

        res = []
        for freq in reversed(freqs):
            for num in freq:
                res.append(num)
                if len(res) == k:
                    return res
