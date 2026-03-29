class Solution:
    def isPalindrome(self, s: str) -> bool:
        # right=len(s)-1
        # left=0
        # s=s.lower()
        # while left<right :
        #     while s[left].isalnum() ==False and left<right:
        #         left +=1
        #     while s[right].isalnum() ==False and left<right :
        #         right -=1
             
        #     if s[left]!=s[right]:
        #         return False
        #     else:
        #         left +=1
        #         right -=1
        # return True

        # newstr=""

        # for a in s :
        #     if a.isalnum():
        #         newstr +=a.lower()
        # return newstr == newstr[::-1] # this is with inbuilt function and extraspace

        left, right =0 ,len(s)-1
        s=s.lower()
        while left<right:
            
            while left < right and not self.isalpha(s[left]):
                left +=1
            while left < right and not self.isalpha(s[right]) :
                right -=1

            if s[left] !=s[right]:
             return False

            left +=1
            right -=1
        return True

    def isalpha(self, a):
        return (( ord('A') <= ord(a) <=ord('Z')) or
         (ord('a') <= ord(a) <= ord('z')) or 
         (ord('0') <= ord(a) <= ord('9')))
            

