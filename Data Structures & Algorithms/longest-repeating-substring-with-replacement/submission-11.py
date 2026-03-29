class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute force
        res=0
        for i in range(len(s)):
            mymap={}
            maxrepeat=0
            for j in range(i,len(s)):
                mymap[s[j]] = 1+mymap.get(s[j],0)
                maxrepeat=max(maxrepeat, mymap[s[j]])
                if(j-i+1-maxrepeat <=k):
                    res=max(j-i+1, res)
                else:
                    break
        return res
                
                
