class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path = set()
        def dfs(perm):

          if len(perm) == len(nums):
            res.append(perm.copy())
            return

          for j in range(len(nums)):
            if nums[j] not in path:
               path.add(nums[j])
               perm.append(nums[j])

               dfs(perm)

               perm.pop()
               path.remove(nums[j])

          return
        dfs([])
        return res
            
            


          
          
