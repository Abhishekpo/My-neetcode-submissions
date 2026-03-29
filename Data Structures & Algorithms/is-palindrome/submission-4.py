class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        left=0
        while left<right :
            s=s.lower()
            while s[left].isalnum() ==False and left<right:
                left +=1
            while s[right].isalnum() ==False and left<right :
                right -=1
             
            if s[left]!=s[right]:
                return False
            else:
                left +=1
                right -=1
        return True
