# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(p,q,root):
            if not root:
                return None
            if root==p:
                return p
            if root==q:
                return q
            
            left = dfs(p,q,root.left)
            right = dfs(p,q,root.right)

            if left==None:
                return right
            elif right==None:
                return left
            elif left and right:
                return root
        
        return dfs(p,q,root)