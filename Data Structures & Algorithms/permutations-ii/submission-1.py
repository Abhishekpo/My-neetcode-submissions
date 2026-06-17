class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        mydict = defaultdict(int)
        for n in nums:
            mydict[n] += 1

        perm =[]
        res=[]
        def dfs():

            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for count in mydict:
                if mydict[count] > 0:
                    perm.append(count)
                    mydict[count] -=1
                    dfs()
                    mydict[count] +=1
                    perm.pop()
        dfs()
        return res
        



            