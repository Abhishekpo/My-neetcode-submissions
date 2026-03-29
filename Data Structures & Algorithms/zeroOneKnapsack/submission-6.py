class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        mem=[[-1]*(capacity+1) for i in range(len(weight)+1)]
        def dfs(i, cap):
            if(i==len(weight) ):
                return 0
            
            if(mem[i][cap]) !=-1:
                return mem[i][cap]
            left=0
            if(weight[i]<=cap):
             left=profit[i]+ dfs(i+1, cap-weight[i])

            right=dfs(i+1, cap)
            mem[i][cap]=max(left, right)
            return mem[i][cap]
        return dfs(0,capacity)

