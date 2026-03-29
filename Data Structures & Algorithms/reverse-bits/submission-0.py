class Solution:
    def reverseBits(self, n: int) -> int:
        
        res=0
        count=0
        while n :
            temp=0
            if n & 1:
               temp= 1<<31-count
               res= res | temp
            n=n>>1
            count +=1
        return res
