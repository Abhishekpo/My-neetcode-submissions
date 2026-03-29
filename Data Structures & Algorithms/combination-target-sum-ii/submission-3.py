class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        myset=set()
        def dfs(i, total, curr):
            if(total==target): # it is very crusial to do this line first because 
                               # the recursion starts with 0 and takes 1st element 
                               # by default and checks it in another call 
                mytup=tuple(curr)
                myset.add(mytup)
                return

            if(i>=len(candidates) or total>target):
                return
            
            print(candidates[i])    
            curr.append(candidates[i])
            dfs(i+1, total+candidates[i], curr) # think why it starts with i+1=1 not i=0
            curr.pop()
            dfs(i+1, total, curr)

        dfs(0,0,[]) # if not checked above codition first then we have to start recursion with
                    #dfs(-1, 0,[]) # even though it starts with last element 
                    # it passes all the test in this case since we can check that element
                    #first. 
        res=[]
        print(myset)
        for c in myset:
            res.append(list(c))
        return res




            