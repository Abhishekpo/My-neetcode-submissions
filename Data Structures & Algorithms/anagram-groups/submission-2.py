class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # i can make a hasmap .
        myhashmap={}
        res=[]

        #start first for loop and sort each element and put it in hashmap
        for i in range(len(strs)):
            sortedst="".join(sorted(strs[i]))
            if sortedst in myhashmap:
                myhashmap[sortedst].append(strs[i])
            else:
                myhashmap[sortedst]=[strs[i]]
        for values in myhashmap.values():
            res.append(values)
        return res
         

        # start another for loop and check from next index if the sorted in 
        # in the hashmap and if yes put it in a list

        # comeout of the 2nd loop and add the res to the list
        
        # return the list