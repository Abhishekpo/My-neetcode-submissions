class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        myset=set()
        list1=[]
        def dfs(i, myset, list1):

            if(len(nums)==len(list1)):
                res.append(list1.copy())
                return

            for j in range(len(nums)):
                if nums[j] not in myset:
                 myset.add(nums[j])
                 list1.append(nums[j])
                 dfs(j+1, myset, list1)
                 myset.remove(nums[j])
                 list1.pop()
                 
        dfs(0, myset, list1)
        return res

                