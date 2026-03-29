class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        checker=strs[0]
        minPrefixcount=len(checker)
    
        for i in range(1, len(strs)):
            prefixcount =0
            length=min(len(strs[i]), len(checker))
            for j in range(length):
                if(checker[j]!=strs[i][j]):
                    break
                prefixcount +=1
            minPrefixcount=min(minPrefixcount, prefixcount)
        return checker[:minPrefixcount] if minPrefixcount !=0 else ""
            
                

            