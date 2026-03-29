class Solution:
    def mySqrt(self, x: int) -> int:

        L=0
        R=x
        while L<=R:
            mid=(L+R)//2
            if mid*mid==x:
                return mid
            elif mid*mid > x:
                R =mid-1
            else:
                L =mid+1

        return R