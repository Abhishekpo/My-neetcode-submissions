# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 0
        prev=head

        while curr:
            count  +=1
            curr = curr.next
        
        n = count-n
        curr = head
        count = 0
        prev=head
        while curr:
            if count == n:
                break
            count +=1
            prev=curr
            curr=curr.next

        if curr == head:
            head=head.next
        else:
         prev.next=curr.next

        return head
        


        
