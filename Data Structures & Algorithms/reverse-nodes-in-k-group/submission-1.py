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

            node_k = findkthnode(tmp, k)

            if not node_k:
                if prevnode:
                    prevnode.next = tmp
                break

            nextnode = node_k.next

            node_k.next = None

            reverse(tmp)
            if tmp == head:
                head = node_k
            else:
                prevnode.next = node_k

            prevnode = tmp
            tmp = nextnode

        return head