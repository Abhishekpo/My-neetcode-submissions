class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans=0
        res=""        
        
        def checkPlaindrome(st):

            l=0
            r=len(st)-1

            while l<=r:
                if st[l]==st[r]:
                    l +=1
                    r -=1
                else:
                    return False
            return True
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if(checkPlaindrome(s[i:j])):
                    if ans < len(s[i:j]):
                        ans=len(s[i:j])
                        res=s[i:j]
        return res


