# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity - O(N)
    # Space Complexity - O(N) in the worst case if the tree is linked list
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def find_height(head):
            if not head:
                return 0
            left_height = find_height(head.left)
            right_height = find_height(head.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)
        return find_height(root) != -1
