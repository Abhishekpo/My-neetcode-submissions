class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newans=[]
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            newstart=newInterval[0]
            newend=newInterval[1]
            if newend<start:
                newans.append(newInterval)
                return newans+intervals[i:]
            elif newstart> end:
                newans.append(intervals[i])
            else:
               # newans.append() we dont want to append it yet because we dont know that
               # the future values might also overlap with it 
               newInterval=[min(start, newstart), max(end, newend)]
        
        newans.append(newInterval) # we have to do this to include if it merge at the end
        return newans
               
