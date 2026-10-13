# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(root,subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if root and not subRoot:
                return False
            subleft = match(root.left, subRoot.left)
            subright = match(root.right, subRoot.right)

            if (subleft and subright):
                return root.val == subRoot.val
            elif not (subleft and subright):
                return False
        
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False


        if root.val == subRoot.val:
            if match(root,subRoot):
                return True
  
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        if left or right:
            return True
        
        return False


