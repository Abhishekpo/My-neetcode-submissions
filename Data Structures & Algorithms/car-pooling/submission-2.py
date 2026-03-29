class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        if trips[0][0]>capacity or trips[0][2]<trips[0][1]:
            return False
        totalcap=trips[0][0]
        for i in range(1, len(trips)):
            
            if trips[i][0]>capacity or trips[i][2]<trips[i][1]:
                return False

            if trips[i-1][2]>trips[i][1]:
                if totalcap+trips[i][0]> capacity:
                    return False
                totalcap +=trips[i][0]
            else:
                totalcap =trips[i][0]


        return True
            