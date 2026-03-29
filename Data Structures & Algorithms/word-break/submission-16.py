class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        myset=set(wordDict)
        mem=[None]*(len(s)+1)

        def dfs(i):

            if(i==len(s)):
                return True

            if mem[i] != None:
                return mem[i]
            
            res=dfs(i+1)
            
            for j in range(i, len(s)):
                if s[i:j+1] in myset:
                    if dfs(j+1):
                        mem[i]= True
                        return True
                       
            res=False
            mem[i]=res
            return res
      
        return  dfs(0)
        