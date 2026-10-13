# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        minheap = []
        if not(lists):
            return None
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap,(lists[i].val,i,lists[i]))

        dummynode = ListNode(-1)
        tmp = dummynode
        while minheap:
            val, i, node = minheap[0]
            tmp.next = node
            heapq.heappop(minheap)
            if node.next:
                heapq.heappush(minheap,(node.next.val,i,node.next))
            tmp=tmp.next
        return dummynode.next