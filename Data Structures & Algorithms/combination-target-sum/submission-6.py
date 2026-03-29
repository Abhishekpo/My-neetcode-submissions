class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, list1, total):

            if total==target:
             res.append(list1.copy())
             return

            if i>=len(nums) or total > target:
                 return
            

            list1.append(nums[i])

            dfs(i, list1, total+nums[i])
            list1.pop()
            dfs(i+1, list1, total)

            return res
        return dfs(0, [], 0)
        
