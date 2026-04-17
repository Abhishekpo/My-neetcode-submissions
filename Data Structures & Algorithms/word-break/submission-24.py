class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem={}
        def dfs(i): # can we break the string starting from here in a valid way

            if i==len(s):
                return True
            if i in mem:
                return mem[i]
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict: # # if current substring is valid, check if the remaining string can be broken
                    if dfs(j):# go check for the rest of the string
                        mem[i]=True
                        return True
                    
            mem[i]=False
            return False

        return dfs(0)


