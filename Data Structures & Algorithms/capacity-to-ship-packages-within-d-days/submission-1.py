class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        L=max(weights)
        R=sum(weights)
        res=R
        while L<=R:
            day=1
            totalweight=0
            capacity=(L+R)//2
            i=0
            while i < len(weights): # This is the way to compare if we dont want to
            # include the next weight from the rray
                totalweight +=weights[i] 
                if totalweight  > capacity:
                    day +=1
                    totalweight =0
                    i -=1
                # if we do this at first 
                i +=1

            if day> days:
                L =capacity+1

            else:
                res=min(res, capacity)
                R =capacity-1
            
        return res


            
            
                
                    