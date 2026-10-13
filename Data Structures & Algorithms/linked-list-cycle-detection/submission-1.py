# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        save = {}
        while head:
            save[head] = 1
            head = head.next
            if head in save:
                return True
            if head == None:
                return False
        return False