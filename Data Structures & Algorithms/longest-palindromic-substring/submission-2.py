class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        reslen=0
        for i in range(len(s)):
            #odd palindrome check
            l ,r=i,i
            while l>=0 and r <len(s) and s[l]==s[r]:
                               # this condition needs to be checked first 
                              # before entering to the while loop because
                              # it is the case to stop executing the while loop
                    if(r-l+1)>reslen:
                        res=s[l:r+1] # we are updating res everytime we see palindrome
                        reslen=r-l+1 # updating length everytime 
                      
                    l=l-1
                    r=r+1 
            # even palindrome check
            l, r=i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                    if(r-l+1)>reslen:
                     res=s[l:r+1]
                     reslen=r-l+1
                    l=l-1
                    r=r+1

        return res
