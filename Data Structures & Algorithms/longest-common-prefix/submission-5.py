class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <2:
            return strs[0]
        mincount=float('inf')
        word1=strs[0]
        for i in range(1, len(strs)):
            j=0
            count=0
            while j<len(word1) and j<len(strs[i]):
                if(word1[j]!=strs[i][j]):
                    break
                count +=1
                j+=1
            mincount=min(mincount, count)
        return word1[:mincount] if mincount !=float('inf') else ""