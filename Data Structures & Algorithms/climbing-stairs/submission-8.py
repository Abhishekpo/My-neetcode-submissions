class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        i=3
        one=1
        two=2
        while i<=n:
            temp= two
            two= one + two
            one=temp
            i +=1
        return two 


     

            