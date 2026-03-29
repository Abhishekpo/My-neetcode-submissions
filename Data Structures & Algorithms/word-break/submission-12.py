class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        myset=set(wordDict)
        mem=[None]*(len(s)+1)

        def dfs(i):

            if(i==len(s)):
                return True

            if mem[i] != None:
                return mem[i]
            
            for j in range(i, len(s)):
                if s[i:j+1] in myset:
                    if dfs(j+1):
                        mem[i]= True
                        return True
                       
                        
            mem[i]=False
           
        dfs(0)
        return mem[0]
        