class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        prev = float("-inf")
        for start, end in sorted(intervals):
            if start >= prev:
                prev = end
            else:
                count += 1
                prev = min(prev, end)
        
        return count
