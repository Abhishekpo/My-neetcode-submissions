class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # myset=set()
        # mylist=[]
        
        # if nums ==[0,0,0]:
        #  return [[0,0,0]]
        # for n in nums:
        #     myset.add(n)
        
        # for left in range(len(nums)-2):

        #     for right in range(left+1, len(nums)-1):
        #         twoSum= nums[left]+nums[right]
        #         twoSum = -1*twoSum
        #         if twoSum in myset and left != nums.index(twoSum) and right !=nums.index(twoSum):
        #             listtoadd=[nums[left], nums[right], twoSum]
        #             listtoadd=sorted(listtoadd)
        #             if listtoadd not in mylist:
        #                 mylist.append(listtoadd)
        
        # return mylist

        mylist=[]
        nums.sort()

        for i , a in enumerate(nums):

            if i>0 and a== nums[i-1]: # removing duplicate in first position
                continue
            left , right =i+1 , len(nums)-1
            while left<right:
                threesum= nums[i]+nums[left]+nums[right]
                if threesum <0:
                    left +=1
                elif threesum >0:
                    right -=1
                else:
                    mylist.append([nums[i], nums[left],nums[right]])
                    left +=1
                    while nums[left] ==nums[left-1] and left<right: # removing duplicate in left and right
                        left +=1
                

        return mylist


                
