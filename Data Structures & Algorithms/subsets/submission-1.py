class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(i, para):

            if i >= len(nums):
                res.append(para.copy())
                return

            para.append(nums[i])
            
            dfs(i+1, para) 
            para.pop()
            dfs(i+1, para)

        dfs(0, [])
        return res

                