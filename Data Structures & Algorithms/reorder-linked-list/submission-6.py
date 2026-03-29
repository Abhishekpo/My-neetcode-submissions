# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast=head, head

        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next
        
        head2=slow.next
        slow.next=None

        curr2=head2
        prev=None
        while curr2:
            temp=curr2
            curr2=curr2.next
            temp.next=prev
            prev=temp
        
        head2=prev

        curr1=head
        curr2=head2
        while curr1 and curr2:
            temp1=curr1
            temp2=curr2
            curr1=curr1.next
            curr2=curr2.next
            temp1.next=temp2
            temp2.next=curr1

            


