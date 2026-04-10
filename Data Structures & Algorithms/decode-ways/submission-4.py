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

        #Use this in your head:

#“dfs(i) tells me how many valid ways exist from index i.
#At i, I try every valid next move, and for each move I ask recursion to solve the rest.”

        cache=[-1]*len(s)
        def dfs(i): # returns the number of ways to decode s starting from index i

            if(i>=len(s)):
                return 1
            if cache[i] !=-1:
                return cache[i]

            if s[i] =='0':
                return 0
            res=0
            if int(s[i])<10:
                res = dfs(i+1) # if I take one digit, count ways from the next index

            if i+1<len(s):
                 if (int(s[i])==1 or (int(s[i]) ==2 and int(s[i+1]) < 7)):

                    res +=dfs(i+2) # if I take two digits, count ways from index i+2
                        

            cache[i]=res
            return res

        return dfs(0)