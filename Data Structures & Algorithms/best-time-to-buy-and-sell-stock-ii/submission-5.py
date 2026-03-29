class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mem=defaultdict(int)
        n=len(prices)
        mem=[[0]*(n+1) for _ in range(2)] # we can do this way 
        
        for j in range(n-1, -1, -1):
            for i in range(2):
                if i==1:
                 mem[i][j]=max(mem[i][j+1], prices[j]+mem[i-1][j+1])
                else:
                  mem[i][j]=max(mem[i][j+1], -prices[j]+mem[i+1][j+1])
                  
        return mem[0][0]