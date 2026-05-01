class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        globalmax=float('-inf')
        globalmin=float('inf')
        currentmax=0
        currentmin=0
        total=0
        for n in nums:
            currentmax=max(n, currentmax+n)
            currentmin=min(n, currentmin+n)
            total +=n
            globalmax=max(currentmax, globalmax)
            globalmin=min(globalmin, currentmin)

        return max(globalmax, total-globalmin) if globalmax >= 0 else globalmax
        # This is a trick maxcircular_Sum = (total - middlenoncircularsubarray)
        #                 maximize(maxcircular_Sum) = total - minimize(middlenoncircularsubarray)
        #                 maximize(maxcircular_Sum) =  total - globalmin
