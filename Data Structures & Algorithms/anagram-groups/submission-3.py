class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myhash=defaultdict(list)

        for st in strs:
            list1=[0]*26
            for s in st:
                list1[ord(s)-ord('a')] +=1
            list1=tuple(list1)
            myhash[list1].append(st)
        return list(myhash.values())