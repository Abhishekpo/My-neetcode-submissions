class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        seen ={0:1}

        currentSum=0
        count =0
        for n in nums:
            currentSum +=n
            prefixcount = seen.get(currentSum%k , 0)

            count +=prefixcount

            seen[currentSum%k] = 1 + seen.get(currentSum%k, 0)
        return count
            
        