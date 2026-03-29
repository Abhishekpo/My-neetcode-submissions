class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        myset=set(dictionary)
        mem=[-1]*len(s)
        
        def dfs(i):
            
            if(i>=len(s)):
                return 0
            if(mem[i]!=-1):
                return mem[i]

            mem[i] = 1+dfs(i+1)
            
            for j in range(i, len(s)):
                if s[i:j+1] in myset:
                    mem[i]=min(dfs(j+1), mem[i])

            return mem[i]
        return dfs(0)