class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ''' myhash={}
        for num in nums:
            myhash[num] = 1+ myhash.get(num, 0)
        
        myhash=dict(sorted(myhash.items(), key=lambda item:item[1], reverse=True))
        res=[]
        i=0
        for key, value in myhash.items():
                res.append(key)
                i +=1
                if i>=k:
                    return res'''
        
        myhash={}
        for num in nums:
            myhash[num] = 1+ myhash.get(num, 0)
        
        hash1=[[] for i in range(len(nums)+1)]

        for key, value in myhash.items():
            hash1[value].append(key)
        
        res=[]
        j=0
        for i in range(len(hash1)-1,0,-1):
            for has in hash1[i]:
                res.append(has)
                j +=1
                if j>=k:
                    return res
                




            
    



        # bucket sort O(n)

        
            
        
            