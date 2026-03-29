class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length=0
        L=0
        R=0
        newset=set()
        while R<len(s):
            if s[R] in newset:
                while s[L] !=s[R]:
                    newset.remove(s[L])
                    L +=1
                newset.remove(s[L])
                L +=1

            newset.add(s[R])
            length=max(len(newset), length)
            R +=1
        return length
