class Solution:
    def findMin(self, nums: List[int]) -> int:
        right=len(nums)-1
        left=0
        while left<right:
            mid= (left+right)//2
            if nums[mid] > nums[right]: #and nums[mid] >nums[right] and mid !=right and mid !=left:
                left=mid+1
            else: #and nums[mid]<nums[right] and mid !=right and mid !=left:
                 right = mid
            #else:
                #if nums[mid] == nums[left] and nums[mid] > nums[right]:
                   # left = mid+1
                #else:
                    #right =mid-1
        return nums[right]
            
        