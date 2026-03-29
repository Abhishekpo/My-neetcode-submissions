class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        def dfs(i, curr, total):
            
            if(i>= len(nums) or total > target ):
                return
            total +=nums[i]
            curr.append(nums[i])

            if(total==target):
                res.append(curr.copy())
                

            dfs(i, curr, total )
            curr.pop()
            total -=nums[i]
            dfs(i+1, curr, total)
        dfs(0,[],0)
        return res