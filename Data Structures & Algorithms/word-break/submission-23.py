class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem={}
        def dfs(i): # can we break the string starting from here in a valid way

            if i==len(s):
                return True
            if i in mem:
                return mem[i]
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict: # if string in the dict go and check for the rest of the string
                    if dfs(j):# go check for the rest of the string
                        mem[j]=True
                        return mem[j]
                    
            mem[i]=False
            return mem[i]

        return dfs(0)


