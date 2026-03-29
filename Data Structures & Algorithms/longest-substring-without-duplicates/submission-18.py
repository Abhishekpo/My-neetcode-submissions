class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        myset=set()
        L=0
        res=0
        for R in range(len(s)):
            if s[R] in myset:
                while s[R] in myset:
                    myset.remove(s[L])
                    L+=1

            myset.add(s[R])
            res=max(res, len(myset))
        return res

