class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        myset=set(wordDict)
        mem=[None]*(len(s)+1)
        mem[len(s)]=True

        def dfs(i):

            if mem[i] != None:
                return mem[i]
                
            dfs(i+1)
            for j in range(i, len(s)):
                if s[i:j+1] in myset:
                    if(dfs(j+1)):
                     mem[i]=mem[i+len(s[i:j+1])]
                     return
           
            mem[i]=False
        dfs(0)
        return mem[0]
        