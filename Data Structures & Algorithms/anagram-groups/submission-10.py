class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict=defaultdict(list)
        for st in strs:
            mylist=[0]*26
            for s in st:
                mylist[ord('a')-ord(s)] +=1
            mydict[tuple(mylist)].append(st)
        return list(mydict.values())


