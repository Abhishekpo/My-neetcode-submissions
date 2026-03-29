"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i:i.start)
        if not intervals:
            return True
        currentend=intervals[0].end
        for interval in intervals[1:]:
            start=interval.start
            end=interval.end
            if currentend > start:
                return False
            else:
                currentend=end

        return True
