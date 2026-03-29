class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         # one approach is to pick the first string and 
         # comapre its character one  y one with all the strings
         # if anyone doesn't match return the collected string immidiately

         res=""
         for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or strs[0][i] !=s[i]:
                    return res
            res +=strs[0][i]
         return res