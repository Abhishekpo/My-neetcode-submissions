class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        myset1=set(nums1)
        myset2=set(nums2)
        ans=[]
        ans_set1=set()
        for num in nums1:
            if num not in myset2:
                ans_set1.add(num)

        ans.append(list(ans_set1))
        ans_set2=set()
        for num in nums2:
            if num not in myset1:
                ans_set2.add(num)
        ans.append(list(ans_set2))
        return ans



            