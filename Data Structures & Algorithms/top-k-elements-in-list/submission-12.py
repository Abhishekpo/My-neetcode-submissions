class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket=[[] for i in range(len(nums)+1)]
        hashmap={}
        res=[]
        for n in nums:
            hashmap[n] =1+hashmap.get(n,0)
        for key, value in hashmap.items():
            bucket[value].append(key)
        for i in range(len(bucket)-1, 0,-1):
            '''if not bucket[i]: optional/not needed
                continue'''
            for c in bucket[i]:
                res.append(c)
                if len(res)==k:
                    return res
                #else: optional/ not needed
                
       # return res not nneeded
