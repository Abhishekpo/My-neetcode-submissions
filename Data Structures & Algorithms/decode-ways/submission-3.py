class Solution:
    def numDecodings(self, s: str) -> int:
        # 12=> AB or L
        #01 =>0 since its invalid
        # 123467 => if it is from 1 to 9 it can be decoded 1 ways for sure
        # but when we get something after 1 and 2 then we could decode it 
        # for example 12 13 => l M
        # I alsways have to check two letters 1st and after that
        # first will always be counted as 1 if it is not 0 
        # the second will be counted as 2 if it is between 0-6
        cache=[-1]*len(s)
        def dfs(i):# go find me total number of possible ways to decode strting at i

            if(i>=len(s)):
                return 1
            if cache[i] !=-1:
                return cache[i]

            if s[i] =='0':
                return 0

            if int(s[i])<10:
                res = dfs(i+1) # go find me starting at i+1
            
            if i+1<len(s):
                 if (int(s[i])==1 or (int(s[i]) ==2 and int(s[i+1]) < 7)):
                    res +=dfs(i+2) # go find me starting at i+2
                        

            cache[i]=res
            return res

        return dfs(0)