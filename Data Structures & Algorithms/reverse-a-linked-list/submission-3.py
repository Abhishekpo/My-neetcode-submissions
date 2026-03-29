# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current= head
        prev=None
        if not head:
         return None

        while current:
            temp=prev
            prev=current
            current=current.next
            prev.next=temp
        
        return prev
