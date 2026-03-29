class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      mydic1={}
      mydic2={}
      if(len(s)!=len(t)):
        return False
      for ch in s:
        mydic1[ch]=1+mydic1.get(ch,0)
      for ch in t:
        mydic2[ch]=1+mydic2.get(ch,0)

      return mydic1==mydic2

      
    
