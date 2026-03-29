class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result=[]

        for i, n in enumerate(nums):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            L=i+1
            R=len(nums)-1
            while L<R:
                sum3=nums[i]+nums[L]+nums[R] 
                if sum3>0:
                    R -=1
                elif sum3<0:
                    L +=1
                    
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L +=1
                    R-=1
                    while nums[L]==nums[L-1] and L<R:
                        L+=1
                    
        return result
                


