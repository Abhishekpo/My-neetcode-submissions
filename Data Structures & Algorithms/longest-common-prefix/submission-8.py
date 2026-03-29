class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # next approach is we can make first as a dummy prefix 
        # and keep updating prefix on the way
        

        prefix=strs[0]

        for i in range(1, len(strs)):
            j=0
            while j< min(len(prefix), len(strs[i])):
                if(prefix[j]!=strs[i][j]):
                    break
                j+=1
            prefix=prefix[:j]

        return prefix
