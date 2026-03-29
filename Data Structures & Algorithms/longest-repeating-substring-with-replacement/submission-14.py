class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        countFreq={}
        L=0
        res=0
        for R in range(len(s)):
            countFreq[s[R]] =1+ countFreq.get(s[R], 0)
            maxfreq= max(countFreq.values())

            if (R-L+1 - maxfreq) <=k:
                res=max(R-L+1, res)
            else:
                countFreq[s[L]]-=1
                L +=1

        return res
