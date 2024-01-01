# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder(self, root) -> None:
            if not root:
                return None 
            inorder(self, root.left)
            arr.append(root.val)
            inorder(self, root.right)
        inorder(self, root)
        return arr
         
        
        
        