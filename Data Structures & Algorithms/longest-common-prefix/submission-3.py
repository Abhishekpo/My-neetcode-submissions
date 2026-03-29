class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        word1=strs[0]
        mincount=0
        for i in range(1, len(strs)):
            j=0
            while j<len(word1) and j<len(strs[i]):
                if(word1[j]!=strs[i][j]):
                    break
                j+=1
            word1=word1[:j]
            
        return word1