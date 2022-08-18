# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(current,left,right):
            if not current:
                return True
            if not (current.val>left and current.val<right):    
                return False
            return (valid(current.left,left,current.val) and valid(current.right,current.val,right))
        return valid(root,float("-inf"),float("inf"))