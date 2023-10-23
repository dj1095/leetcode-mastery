# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity - O(N) since we visits each element only once
    # Space Complexity - O(logN) since max depth of tree is logN
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def arr_to_bst_recursive(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = arr_to_bst_recursive(left, mid - 1)
            root.right = arr_to_bst_recursive(mid + 1, right)
            return root
        return arr_to_bst_recursive(0, len(nums) - 1)
