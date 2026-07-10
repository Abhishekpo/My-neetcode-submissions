class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        # brute force:
            1: first from every index start building a subarray and while adding
            each subarray check that new element with every element in that sub arry
            for the limit constraints. 
            2: if the constraint meets add it to the subarray else start new subarray
            from another index
            3: [10, 1,2,4,7,2] limit 5
            [10]
            [10,1] invalid so start new subaray with new index 
            [1,2,4]
            [1,2,4,7] invalid so newstart
            [2]
            [2,4] ...
            [2,4,7,2] this is the answer

            [4,7,2]
            []
            
            so from here we can see that we can use sliding window to code this
            left pointer and right pointer moves ahead by keeping track of
            current_max and current_min and find current_max - current_min <= limit and as soon as it encounters
            a invalid element it breaks. and restart the pointer by shifting l by one
            and repeat the process again.

            but doing this also needs a lot of repeated work becaue we have to come back
            and process the same index again and again:
            for example: After making this subarray [1,2,4,7] 
            we come back and again start building from 2 [2] [2,4] [2,4,7] [2,4,7,2]

            so this is also not optimal because O(n^2)

            so optimal way should be to keep track of max and min of the subarray
            which we can do by keeping track of monotonic queues.
            
            keep max and min queue from left of the nums and keep track 

        """
        max_queue = deque()
        min_queue = deque()

        l=0
        res =0
        for r in range(len(nums)):
            while max_queue and max_queue[-1] < nums[r]:
                max_queue.pop()
            while min_queue and min_queue[-1] > nums[r]:
                min_queue.pop()
            
            max_queue.append(nums[r])
            min_queue.append(nums[r])

            if abs(max_queue[0] - min_queue[0]) > limit:
                if nums[l] == max_queue[0]:
                    max_queue.popleft()

                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                l +=1
            res = max(res, r-l+1)
        return res
                
                
        

    
        