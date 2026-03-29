class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False

        n=x
        ans=0
        while n>0:
            remainder= n%10
            ans = (ans*10) + remainder
            n=n//10

        if ans==x:
            return True
        
        return False
            
