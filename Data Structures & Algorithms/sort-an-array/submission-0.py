class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        L=0
        R=len(nums)-1
        result=[]
        def mergeDivide(L, R):
            if(R-L+1 ==1): # if length is 1 return no further division
                return
            mid=(R+L)//2
            mergeDivide(L, mid)
            mergeDivide(mid+1, R)

            merge(L, R, mid)

        def merge(L, R, mid):
            left=nums[L:mid+1]
            right=nums[mid+1:R+1]
            temp=[]

            i=0
            j=0
            k=L
            while i<len(left) and j<len(right):
                if(left[i]<right[j]):
                    temp.append(left[i])
                    i+=1
                else:
                    temp.append(right[j])
                    j +=1
            while i<len(left):
                temp.append(left[i])
                i+=1
            while j<len(right):
                temp.append(right[j])
                j +=1
            i=0
            while k<=R and i<len(temp):
                nums[k]=temp[i]
                k +=1
                i+=1
            
        mergeDivide(L, R)
        return nums
                
