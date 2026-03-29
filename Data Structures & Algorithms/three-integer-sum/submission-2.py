class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        myset=set()
        mylist=[]
        
        if nums ==[0,0,0]:
         return [[0,0,0]]
        for n in nums:
            myset.add(n)
        
        for left in range(len(nums)-2):

            for right in range(left+1, len(nums)-1):
                twoSum= nums[left]+nums[right]
                twoSum = -1*twoSum
                if twoSum in myset and left != nums.index(twoSum) and right !=nums.index(twoSum):
                    listtoadd=[nums[left], nums[right], twoSum]
                    listtoadd=sorted(listtoadd)
                    if listtoadd not in mylist:
                        mylist.append(listtoadd)
        
        return mylist

                
