"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        prevs = [-1]
        for interval in sorted(intervals, key=lambda interval: (interval.start, interval.end)):
            new_room = True
            for i, prev in enumerate(prevs):
                if interval.start >= prev:
                    prevs[i] = interval.end
                    new_room = False
                    break
            if new_room:
                prevs.append(interval.end)
        return len(prevs)
