class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L=0
        minval=nums[0]
        R=len(nums)-1
        
        while L<=R:
            if nums[L]< nums[R]:
                minval=min(minval, nums[L])
                break
            mid=(R+L)//2
            if(nums[mid] <= nums[R]):
                R=mid-1
            else:
                L=mid+1
            minval=min(nums[mid], minval)
        return minval


                    
                
