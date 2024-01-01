# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        
        def inorder(self, root) -> None:
            if not root:
                return
            inorder(self, root.left)
            arr.append(root.val)
            inorder(self, root.right)
            
        inorder(self, root)
        return arr[k-1]
            
        
        