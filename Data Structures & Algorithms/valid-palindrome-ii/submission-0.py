class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s==s[::-1]:
            return True
        
        for i in range(len(s)):
            newstr=s[:i]+s[i+1:]
            if newstr==newstr[::-1]:
                return True
        return False
            