class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval)
        current = intervals[0]
        res = []
        for interval in intervals:
            if current[1] < interval[0]:
                res.append(current)
                current = interval
            else:
                current = [min(current[0], interval[0]), max(current[1], interval[1])]
        res.append(current)
        
        return res
