# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        start=list1
        if not list1:
            return list2
        if not list2:
            return list1
        if(curr1.val<curr2.val):
            start=curr1
            curr1=curr1.next
        else:
            start=curr2
            curr2=curr2.next
        while curr1 and curr2:
            if(curr1.val <curr2.val):
                temp=curr1.next
                start.next=curr1
                curr1=temp
            else:
                temp=curr2.next
                start.next=curr2
                curr2=temp
            start=start.next

        if curr1:
            start.next=curr1
        if curr2:
            start.next=curr2
        
        return list1 if list1.val <list2 .val else list2


            