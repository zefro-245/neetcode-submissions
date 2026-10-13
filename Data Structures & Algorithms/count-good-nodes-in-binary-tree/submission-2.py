# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0
        maxsofar = root.val
        def count(root, maxsofar):
            nonlocal c
            if not root:
                return 0
            if root.val >= maxsofar:
                maxsofar = root.val
                c+=1
            left = count(root.left,maxsofar)
            right = count(root.right,maxsofar)
            return root
        count(root,maxsofar)
        return c