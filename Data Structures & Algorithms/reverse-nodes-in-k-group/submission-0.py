class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def findkthnode(node, k):
            curr = node

            for _ in range(k - 1):
                if not curr:
                    return None
                curr = curr.next

            return curr

        def reverse(node):
            prev = None
            curr = node

            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode

            return prev

        tmp = head
        prevnode = None

        while tmp:

            # Find kth node of current group
            node_k = findkthnode(tmp, k)

            # Fewer than k nodes remain
            if not node_k:
                if prevnode:
                    prevnode.next = tmp
                break

            # Save beginning of next group
            nextnode = node_k.next

            # Disconnect current group
            node_k.next = None

            # Reverse current group
            reverse(tmp)

            # First group
            if tmp == head:
                head = node_k
            else:
                prevnode.next = node_k

            # tmp is now the last node of reversed group
            prevnode = tmp

            # Move to next group
            tmp = nextnode

        return head