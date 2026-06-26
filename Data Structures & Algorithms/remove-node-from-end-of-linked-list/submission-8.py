# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr=head
        count=0

        while curr:
            count +=1
            curr =curr.next

        dest = count - n
        curr = dummy
        while curr and dest > 0:
            curr = curr.next
            dest -=1
        
        curr.next =curr.next.next

        return dummy.next
             