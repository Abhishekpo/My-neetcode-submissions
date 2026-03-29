"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mydict={None:None}
        curr=head
        while curr:
            mydict[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        dummy=Node(-1)
        tail=dummy
        while curr:
            tail.next=mydict[curr]
            tail.next.random=mydict[curr.random]
            tail=tail.next
            curr=curr.next
        return dummy.next