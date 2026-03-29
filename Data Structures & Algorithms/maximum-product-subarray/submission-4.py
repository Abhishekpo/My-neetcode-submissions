class Solution:
    def maxProduct(self, nums: List[int]) -> int:
           maxSum, minSum =1 ,1
           res=-1e9
           for n in nums:
            temp=maxSum
            maxSum=max( maxSum*n, minSum*n, n)
            minSum=min(temp*n, minSum*n, n)
            res=max(res, maxSum)

           return res


           
            


