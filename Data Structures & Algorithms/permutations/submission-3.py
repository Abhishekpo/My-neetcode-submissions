class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        result=[]
        def dfs(indx):
                if(indx==len(nums)):
                  result.append(nums.copy())
                  return
        
                for j in range(indx, len(nums)):
                    nums[indx], nums[j]=nums[j], nums[indx]
                    dfs(indx+1) # we should always increase index not j here 
                    nums[indx], nums[j]=nums[j], nums[indx]
        dfs(0)
        return result
            



                