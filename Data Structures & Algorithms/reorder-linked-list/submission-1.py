# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current=head
        size=1
        while current:
            current=current.next
            size+=1

        sizeofreplacement=size/2
        sizeofFirstlist=size-sizeofreplacement

        
        current, prev = head, None
        i=1

        while i<sizeofFirstlist:
            current=current.next
            i +=1

        prev=current
       
        current2=current.next
        prev.next=None
        
        prev=None
        while current2:
            temp=current2
            current2=current2.next
            temp.next=prev
            prev=temp
        
        current2=prev


        current =head
        prev=None
        while current and current2:
            prev=current
            current=current.next
            prev.next=current2
            temp=current2
            current2=current2.next
            temp.next=current
            

        


        