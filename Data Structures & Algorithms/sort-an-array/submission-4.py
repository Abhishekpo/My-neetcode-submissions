class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        L=0
        R=len(nums)-1
        def mergeDivide(L, R):
            if(L>=R): # if length is 1 return no further division
                return
            mid=(R+L)//2
            mergeDivide(L, mid)
            mergeDivide(mid+1, R)

            merge(L, R, mid)

        def merge(L, R, mid):
            left=nums[L:mid+1]
            right=nums[mid+1:R+1] 

            i=0
            j=0
            k=L
            while i<len(left) and j<len(right):
                if(left[i]<right[j]):
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j +=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j +=1
                k+=1
            
        mergeDivide(L, R)
        return nums
                
