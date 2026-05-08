"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # line sweep is the best approach for this problem

        map1={}
        for interval in intervals:
            map1[interval.start] = 1 + map1.get(interval.start, 0)
            map1[interval.end] = -1 + map1.get(interval.end, 0)

        res=0
        current=0
        for item in sorted(map1.keys()):
            current += map1[item] # calculating cumulative sum
            res = max(res, current) # and keeping record of the higest value so far

        return res




