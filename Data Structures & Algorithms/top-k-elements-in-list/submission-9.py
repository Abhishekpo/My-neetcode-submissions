class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myhash={}
        for num in nums:
            myhash[num] = 1+ myhash.get(num, 0)
        
        myhash=dict(sorted(myhash.items(), key=lambda item:item[1], reverse=True))
        res=[]
        i=0
        for key, value in myhash.items():
                res.append(key)
                i +=1
                if i>=k:
                    return res
            




        # bucket sort O(n)

        
            
        
            