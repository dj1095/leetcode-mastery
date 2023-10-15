# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #Time Complexity - O(N) where N is total nodes in tree
        #Space Complexity - O(N) Max Recursion Depth
        
        def is_symm_recursive(left_tree , right_tree):
            if not left_tree and not right_tree:
                return True
            elif not left_tree or not right_tree:
                return False
            elif left_tree.val != right_tree.val:
                return False
            return is_symm_recursive(left_tree.left, right_tree.right) and is_symm_recursive(left_tree.right, right_tree.left)
        return is_symm_recursive(root.left, root.right)
        