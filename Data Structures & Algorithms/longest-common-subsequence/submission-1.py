class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m=len(text1)
        n=len(text2)
        cache=[[-1]*n for i in range(m)]

        def dfs(i,j):

            if(i==m or j==n):
                return 0

            if(cache[i][j]!=-1):
                return cache[i][j]
            
            if(text1[i]==text2[j]):
                cache[i][j]=1+dfs(i+1, j+1)
                
            else:
                left= dfs(i+1, j) 
                right=dfs(i, j+1)
                cache[i][j]=max(left, right)

            return cache[i][j]
        return dfs(0,0)

