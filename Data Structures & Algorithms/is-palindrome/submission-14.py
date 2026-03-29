class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalphanum(c):
         if(ord('a')<=ord(c)<=ord('z') or (ord('0')<=ord(c)<=ord('9'))):
             return True
         return False
        
        L=0
        R=len(s)-1

        while L<R:
            while L<R and not isalphanum(s[L].lower()):
                L +=1
            while L<R and not isalphanum(s[R].lower()):
                R -=1
            if s[L].lower() !=s[R].lower():
                return False
            else:
             L +=1
             R -=1
        return True

    

