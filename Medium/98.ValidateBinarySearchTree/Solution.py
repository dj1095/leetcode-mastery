# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity - O(N) since we are visiting every node only once
# space complexity - O(H) due to recursive stack where h is the height of binary tree, H can be N in worst case like given tree is linked list
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, left_boundary, right_boundary):
            if not node:
                return True

            if not (node.val > left_boundary and node.val < right_boundary):
                return False

            return is_valid(node.left, left_boundary, node.val) and is_valid(node.right, node.val, right_boundary)
        return is_valid(root, -math.inf, math.inf)
