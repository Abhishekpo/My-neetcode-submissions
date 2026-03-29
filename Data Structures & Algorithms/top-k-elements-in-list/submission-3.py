class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myhashmap={}
        mylist=[]
        res=[]
        for n in nums:
            myhashmap[n]=1+myhashmap.get(n, 0)

        # newhashmap= dict(sorted(myhashmap.items(), key=lambda item:item[1], reverse=True))
        # keys=list(newhashmap.keys())
        for key, value in myhashmap.items():
            mylist.append((value,key))
        
        mylist.sort()
        for i in range(k):
            res.append(mylist.pop()[1])

        return res