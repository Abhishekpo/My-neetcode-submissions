# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # current=head
        # myset=set()

        # while current:
        #     if current in myset:
        #         return True
        #     else:
        #         myset.add(current)
        #     current=current.next

        # return False

        fast=head.next
        slow=head

        while fast and fast.next:
            if slow ==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False


