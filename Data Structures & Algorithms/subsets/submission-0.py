class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(i, para):

            if i >= len(nums):
                res.append(para.copy())
                return
            
            dfs(i+1, para + [nums[i]])
            dfs(i+1, para)

        dfs(0, [])
        return res

                