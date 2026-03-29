class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mydict={}
        result=[]
        for num in nums:
            mydict[num]=1+mydict.get(num, 0)
        sorted_dict=dict(sorted(mydict.items(), key=lambda x:x[1], reverse=True))
        sorted_keys=list(sorted_dict.keys())
        
        return sorted_keys[:k]