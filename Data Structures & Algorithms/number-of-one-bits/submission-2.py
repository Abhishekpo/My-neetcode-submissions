class Solution:
    def hammingWeight(self, n: int) -> int:
        # we can also do n%2 and make n=n//2
        count=0
        while n:
            if n %2:
                count +=1
            n=n//2
        return count
            