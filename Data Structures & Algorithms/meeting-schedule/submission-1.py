"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev = -1
        for interval in sorted(intervals, key=lambda interval: (interval.start, interval.end)):
            if interval.start < prev:
                return False
            else:
                prev = interval.end
        return True
