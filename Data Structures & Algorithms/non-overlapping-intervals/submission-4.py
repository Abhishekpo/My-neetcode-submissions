class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        current=intervals[0]
        count=0
        for i in range(1, len(intervals)):

            if intervals[i][0] < current[1]: # overlap
                current = [min(current[0], intervals[i][0]), min(current[1], intervals[i][1])]
                count  +=1

            else:
                current=intervals[i]
        return count


