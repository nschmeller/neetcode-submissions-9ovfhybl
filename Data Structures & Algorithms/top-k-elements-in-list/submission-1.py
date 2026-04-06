from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_counts = sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)
        return [pair[0] for pair in sorted_counts[:k]]
