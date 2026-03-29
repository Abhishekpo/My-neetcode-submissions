class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        finalres=[]

        for i in range(len(nums)):
            if i >0 and nums[i] ==nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
               
                
                l=j+1
                r=len(nums)-1
            
                while l<r:
                    total =nums[i]+nums[j]+nums[l]+nums[r]
                    res=[]
                    if total ==target:
                        res.append(nums[i])
                        res.append(nums[j])
                        res.append(nums[l])
                        res.append(nums[r])
                        l +=1
                        r -=1
                        while l<r and nums[r]==nums[r+1]:
                            r -=1
                        
                        finalres.append(res)

                    elif total >target:
                        r-=1
                        while l<r and nums[r]==nums[r+1]:
                            r -=1

                    else:
                        l +=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        return finalres

                    

                
                

            