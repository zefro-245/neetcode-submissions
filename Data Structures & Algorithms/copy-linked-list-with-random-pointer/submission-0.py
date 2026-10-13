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
        tmp = head
        while tmp:
            copy = Node(tmp.val)
            copy.next=tmp.next
            tmp.next=copy
            tmp=tmp.next.next

        tmp=head
        while tmp:
            copy=tmp.next
            if tmp.random:
                copy.random = tmp.random.next
            else:
                copy.random = None
            tmp=tmp.next.next
        
        dummy = Node(-1)
        curr = dummy
        tmp = head

        while tmp:
            copy = tmp.next

            tmp.next = copy.next

            if tmp.next:
                copy.next = tmp.next.next

            curr.next = copy
            curr = curr.next

            tmp = tmp.next

        return dummy.next
