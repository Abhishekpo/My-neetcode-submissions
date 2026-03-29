class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L=0
        myhash={}
        maxrep=0
        res=0
        for R in range(len(s)):
            myhash[s[R]] = 1+myhash.get(s[R],0) 

            maxrep=max(maxrep, myhash[s[R]])

            if(R-L+1 -maxrep <=k):
                res=max(res, R-L+1)

            else:
             myhash[s[L]] -=1
             L+=1

        return res


        
            
