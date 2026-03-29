class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        s=s.lower()
        print(s)
        while L<R:
           if(not (self.isaalpha(s[L]))):
             L+=1
             continue
           if(not (self.isaalpha(s[R]))):
             R-=1
             continue
           if(s[L]!=s[R]):
             return False
           else:
             L +=1
             R -=1

        return True
    def isaalpha(self, c):
        if((ord(c) >= ord('a') and ord(c) <= ord('z') ) or (ord(c)>=ord('0')
         and ord(c)<=ord('9'))):
         return True
        else:
         return False


