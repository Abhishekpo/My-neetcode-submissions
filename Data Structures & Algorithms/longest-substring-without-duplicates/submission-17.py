class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L=0
        R=0
        myset=set()
        maxlength=0
        while R<len(s):
           if s[R] not in myset:
             myset.add(s[R])
             maxlength=max(maxlength, len(myset))
             R +=1

           else:
            while s[R] in myset:
                myset.remove(s[L])
                L +=1
        return maxlength 


