class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        for start, end in sorted(intervals):
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res
