class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        mydicts1=[0]*26
        mydicts2=[0]*26

        for ch in s1:
            mydicts1[ord(ch)-ord('a')] +=1
        L=0
        R=0
        size=len(s2)
        while R<size:
            
            if R-L >=len(s1):
                mydicts2[ord(s2[L])-ord('a')] -=1
                L +=1

            mydicts2[ord(s2[R])-ord('a')] +=1
            R +=1

            if mydicts1==mydicts2:
                return True
            
        return False
            


