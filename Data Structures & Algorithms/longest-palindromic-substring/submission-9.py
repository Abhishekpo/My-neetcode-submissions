class Solution:
    def longestPalindrome(self, s: str) -> str:
        # the best way is to check one element and expad the pointers outwards
        # rathern then inward

        res=""
        length=0

        for i in range(len(s)):
            L, R= i, i
            # for odd length:
            while L>=0 and R<len(s) and s[L]==s[R]:
                if(length<R-L+1):
                    length=R-L+1
                    res=s[L:R+1]
                L-=1
                R+=1
            # for even length
            L, R=i, i+1
            while L>=0 and R<len(s) and s[L]==s[R]:
                if(length<R-L+1):
                    length=R-L+1
                    res=s[L:R+1]
                L -=1
                R +=1
        return res