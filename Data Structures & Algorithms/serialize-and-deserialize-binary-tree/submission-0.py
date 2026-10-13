# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        string = ''
        q = deque()
        q.append(root)

        while q:
            currnode = q.popleft()
            if currnode==None:
                string+='#,'
            else:
                string+=str(currnode.val)
                string+=','
            if currnode!=None:
                q.append(currnode.left)
                q.append(currnode.right)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data)==0:
            return None
        values = data.split(',')[:-1]
        
        i=0
        root = TreeNode(int(values[i]))
        i+=1
        q=deque()
        q.append(root)

        while q:
            node = q.popleft()

            if values[i]=="#":
                node.left = None
            else:
                leftnode = TreeNode(int(values[i]))
                node.left=leftnode
                q.append(leftnode)
            i+=1
        
            if values[i]=="#":
                node.right = None
            else:
                rightnode = TreeNode(int(values[i]))
                node.right=rightnode
                q.append(rightnode)
            i+=1
        return root

        

