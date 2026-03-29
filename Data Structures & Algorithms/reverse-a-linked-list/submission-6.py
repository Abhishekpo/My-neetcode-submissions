# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        prev=None
        dbs=None
        while curr!=None:
            prev=curr
            curr=curr.next
            prev.next=dbs
            dbs=prev
        return prev
            

