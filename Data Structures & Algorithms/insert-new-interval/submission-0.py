class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, before = [], 0
        while before < len(intervals) and intervals[before][1] < newInterval[0]:
            before += 1

        merged = before
        while merged < len(intervals) and intervals[merged][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[merged][0]), max(newInterval[1], intervals[merged][1])]
            merged += 1

        return intervals[:before] + [newInterval] + intervals[merged:]
