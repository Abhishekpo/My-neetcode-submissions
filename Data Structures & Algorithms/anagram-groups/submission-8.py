class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # brute force
        mydict=defaultdict(list)
        for st in strs:
            newst="".join(sorted(st))
            mydict[newst].append(st)
        return list(mydict.values())