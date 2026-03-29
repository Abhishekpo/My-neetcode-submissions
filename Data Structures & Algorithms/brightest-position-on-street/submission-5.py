class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        
        mydict=defaultdict(int)

        for position, rang in lights:
            start=position-rang
            end=position+rang
            mydict[start] +=1 # this light has the effect 
            mydict[end+1] -=1 # because it is inclusive we need to do -1 # this light doesn't affect
        
        lightcount=0
        maxlight=0
        ans=0
        for key in sorted(mydict): # this will give a list of keys
            lightcount +=mydict[key]
            if lightcount > maxlight:
                maxlight =lightcount
                ans=key
        return ans

                

        
        

