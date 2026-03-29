class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        current=intervals[0]
        for i in range(1,len(intervals)):
            if current[1]<intervals[i][0]:
                res.append(current)
                current=intervals[i]
            else:
                current = [min(current[0], intervals[i][0]), max(current[1], intervals[i][1])]
        res.append(current)
        return res


        


