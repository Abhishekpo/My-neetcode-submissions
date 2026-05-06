class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # right now that is my state 
        # I have to check if anything overlaps so
        # I will traverse and check it they do
        # if I see overlap I merge them and and take that merge again and do the same for that
        intervals.sort()
        merge=intervals[0]
        res=[]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] <= merge[1]: # merge
                merge=[min(merge[0], intervals[i][0]), max(merge[1], intervals[i][1])]
            else:
                res.append(merge)
                merge=intervals[i]

        res.append(merge)
        return res


