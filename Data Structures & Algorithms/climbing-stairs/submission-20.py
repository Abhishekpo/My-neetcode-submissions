class Solution:
    def climbStairs(self, n: int) -> int:
        # this is bottom up
        if (n<=2):
            return n

        one=1
        two=2
        for i in range(3, n+1):
            temp=one
            one=two
            two=temp+two

        return two