class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
           
            mydict={}
            L=0
            R =0
            res=0
            while R<len(s):

             mydict[s[R]] =1+mydict.get(s[R],0)

             maxrepeat=max(mydict.values())

             if (R-L+1 - maxrepeat) <=k:
                 res=max(res, R-L+1)
             else:
                mydict[s[L]] -=1
                L+=1

             R+=1
            return res


