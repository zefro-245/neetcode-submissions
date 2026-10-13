# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')
        def dfs(root):
            nonlocal maxsum
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right) 

            current = root.val + max(0, left) + max(0, right) #maxsum with splitting

            maxsum = max(maxsum, current)

            return root.val+max(0,right,left)  #maxsum without splitting

        dfs(root)
        return maxsum
            