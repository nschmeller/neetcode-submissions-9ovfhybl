"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        prevs = []

        for interval in sorted(intervals, key=lambda interval: (interval.start, interval.end)):
            if prevs and prevs[0] <= interval.start:
                heappop(prevs)
            heappush(prevs, interval.end)
        
        return len(prevs)

