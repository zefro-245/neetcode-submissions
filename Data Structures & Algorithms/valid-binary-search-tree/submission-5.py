# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root,lb,ub):
            if not root:
                return True
            if not (root.val>lb and root.val<ub):
                return False
            left = search(root.left,lb,root.val)
            right = search(root.right,root.val,ub)

            return (left and right)
        return search(root,float("-inf"),float("inf"))
