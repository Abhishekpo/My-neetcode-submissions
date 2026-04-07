class Solution:
    def climbStairs(self, n: int) -> int:
        onestep=1
        twostep=1
        for i in range(1,n):
            temp=twostep
            twostep=onestep+twostep
            onestep=temp

        return twostep
        

