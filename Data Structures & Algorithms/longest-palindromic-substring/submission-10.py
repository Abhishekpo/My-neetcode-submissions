class Solution:
    def longestPalindrome(self, s: str) -> str:
       maxlength=0
       maxString=""
       for i in range(len(s)):
        # odd inputs
        l, r= i, i
        while l>=0 and r<len(s) and s[l]==s[r]:
            length= (r-l+1)
            if length>maxlength:
                maxlength=length
                maxString=s[l:r+1]
            l-=1
            r+=1
        # even length:
        l=i 
        r=i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            length= (r-l+1)
            if length>maxlength:
                maxlength=length
                maxString=s[l:r+1]

            l-=1
            r+=1
            
       return maxString