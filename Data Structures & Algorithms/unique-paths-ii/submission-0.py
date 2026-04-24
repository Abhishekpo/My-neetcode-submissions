class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        mem={(row-1, col-1): 1}

        def dfs(i, j):

            if i>=row or j>=col or obstacleGrid[i][j] ==1:
                return 0

            if (i, j) in mem:
                return mem[(i,j)]
            
            mem[(i,j)]=dfs(i, j+1)+dfs(i+1, j)

            return mem[(i, j)]

        return dfs(0,0)
            