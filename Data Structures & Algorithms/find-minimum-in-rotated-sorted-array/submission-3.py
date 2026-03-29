class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L=0
        R=len(nums)-1
        minelem=nums[0]
        while L<=R:
            if nums[L] <=nums[R]:
                minelem=min(minelem, nums[L])
                return minelem
    
            mid=(L+R)//2
            minelem=min(nums[mid], minelem)

            if nums[mid]>=nums[L]: # we are in left half
             L=mid+1
            else:             # we are in right half
             R=mid-1

        return minelem

