# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        length = 0
        curr=head

        copy = ListNode(head.val, head.next)
        curr_copy = copy
        
        while curr_copy:
            length+=1
            curr_copy=curr_copy.next

        while curr:
            count+=1
            if count==length-n:
                curr.next=curr.next.next
                continue
            else:
                curr = curr.next
        if n==length:
            return head.next
        else:
            return head
            