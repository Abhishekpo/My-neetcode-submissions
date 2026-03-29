class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        myhashmap=defaultdict(int)
        for i in range(len(nums)):
            myhashmap[nums[i]] +=1
            if(myhashmap[nums[i]]>len(nums)//2):
                return nums[i]
        
        
