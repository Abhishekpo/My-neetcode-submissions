class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        counteven=0
        for i in range(len(s)):
            # this is for odd
            L=i
            R=i
            while L>=0 and R<len(s) and s[L]==s[R]:
                L-=1
                R +=1
                count +=1
            # this is for even
            
            L=i
            R=i+1
            while L>=0 and R<len(s) and s[L]==s[R]:
                count +=1
                L-=1
                R +=1
        return count
                
