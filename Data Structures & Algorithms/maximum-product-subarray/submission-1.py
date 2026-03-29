class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            totalans=[]
            maxtotal=-1e9
            for i in range(len(nums)):
             ans=[]
             res=1
             for j in range(i, len(nums)):
                ans.append(nums[j])
                res=res*nums[j]
                maxtotal=max(maxtotal, res)
                totalans.append(ans.copy())

            return maxtotal
           
            


