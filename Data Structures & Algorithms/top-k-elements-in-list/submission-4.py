class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myhashmap={}
        mylist= [[] for i in range(len(nums)+1)]
        res=[]
        for n in nums:
            myhashmap[n]=1+myhashmap.get(n, 0)

        # ***newhashmap= dict(sorted(myhashmap.items(), key=lambda item:item[1], reverse=True))
        # **keys=list(newhashmap.keys())

        # without using sortedfunction()
        # for key, value in myhashmap.items():
        #     mylist.append((value,key))
        
        # mylist.sort()
        # for i in range(k):
        #     res.append(mylist.pop()[1])

        # return res

        # using bucketsort

        for key, values in myhashmap.items():
            mylist[values].append(key)
        for i in range(len(mylist)-1,0,-1 ):
            for v in mylist[i]:
                res.append(v)
                if len(res) >=k:
                    break

            if len(res) >=k:
                    break
        return res

