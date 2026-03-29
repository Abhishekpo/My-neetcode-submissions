class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        currentend=intervals[0][1]
        count=0
        for i in range(1, len(intervals)):
            nextstart=intervals[i][0]
            nextend=intervals[i][1]
            if(currentend>nextstart):
                 count +=1
                 currentend=min(currentend, nextend) # we need to remove the element that has 
                                                     # greater length because that might overlap with
                                                     # other element and we are looking for minimum removal.
            else:
                currentend=nextend

        return count
            