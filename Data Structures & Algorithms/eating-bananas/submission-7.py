class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we can't be greedy becaue we don't know what element has what value.
        # okay lets sort is first and then go from the beginning 
        R=max(piles)
        L=1
        res=R
        while L<=R:
            mid=(R+L)//2
            count =0
            for pile in piles:
                count += math.ceil(float(pile)/mid)
            if count >h:
                L =mid+1
            else:
                res=min(res, mid)
                R =mid-1

            
        return res


            
            
                
                

