# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next

        current=second
        prev=slow.next=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
        second=prev
        
        start=head
        while second and head:
            temp=head.next
            head.next=second
            head=temp
            temp2=second.next
            second.next=head
            second=temp2


            
        

