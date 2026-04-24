class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mem={(m-1, n-1):1}
        def dfs(i, j): # number of ways that we can reach end from here

            if i>=m or j>=n:
                return 0

            if (i, j) in mem:
                return mem[(i, j)]
            mem[(i,j)]=dfs(i+1,j) +dfs(i, j+1)
            return mem[(i,j)]

        return dfs(0, 0)

            