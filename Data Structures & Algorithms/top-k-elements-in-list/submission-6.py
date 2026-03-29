class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myhash={}
        for n in nums:
            myhash[n] = 1 + myhash.get(n,0)
        
        myhash=dict(sorted(myhash.items(), key=lambda item:item[1], reverse=True))
        list1=[]
        i=0
        for key, value in myhash.items():
            if i < k:
                list1.append(key)
                i+=1

        return list1
            
        
            