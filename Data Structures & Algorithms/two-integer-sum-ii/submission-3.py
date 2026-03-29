class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         # like 2 sum
         mydict=defaultdict(int)
         for i in range(len(numbers)):
            diff=target-numbers[i]
            if mydict[diff]:
                return [mydict[diff], i+1]
            mydict[numbers[i]]=i+1
        
