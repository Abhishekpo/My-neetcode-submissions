class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, total, totalwt):

           
            if(totalwt>capacity):
                return 0
            if(i>=len(weight)):
                return total

            return max(dfs(i+1, total+profit[i], totalwt+weight[i]), dfs(i+1, total, totalwt))
        return dfs(0,0,0)

